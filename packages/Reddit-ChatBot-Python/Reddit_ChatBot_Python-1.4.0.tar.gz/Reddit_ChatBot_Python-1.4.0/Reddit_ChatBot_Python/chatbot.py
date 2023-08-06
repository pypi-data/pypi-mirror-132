from .ws_client import WebSockClient
import pickle
from .reddit_auth import _RedditAuthBase
from websocket import WebSocketConnectionClosedException
from ._api.tools import Tools
from ._api.models import Channel, Message, BannedUsers, Members
from ._api.iconkeys import Snoo, Reaction
from typing import Dict, List, Optional, Callable, Union
from ._utils.frame_model import FrameType, FrameModel
from ._events import Events


def _get_locals_without_self(locals_) -> dict:
    del locals_['self']
    return locals_


_hook = Callable[[FrameModel], Optional[bool]]


class ChatBot:
    def __init__(self, authentication: _RedditAuthBase, store_session: bool = True,
                 log_error_frames=True, **kwargs):
        self.__r_authentication = authentication
        self._store_session = store_session
        if store_session:
            sb_access_token, user_id = self._load_session(authentication._get_repr_pkl())
        else:
            reddit_authentication = self.__r_authentication.authenticate()
            sb_access_token, user_id = reddit_authentication['sb_access_token'], reddit_authentication['user_id']

        self.__tools = Tools(self.__r_authentication)
        self.__WebSocketClient = WebSockClient(access_token=sb_access_token, user_id=user_id,
                                               get_current_channels=self.__tools.get_channels, **kwargs)
        self.__tools.session_key_getter = self.__WebSocketClient.session_key_getter
        self.event = Events(self.__WebSocketClient)

        if log_error_frames:
            self.event.on_any(func=lambda resp: self.__WebSocketClient.logger.error(resp), frame_type=FrameType.EROR,
                              run_parallel=True)

    def get_own_name(self) -> str:
        return self.__WebSocketClient.own_name

    def get_chatroom_name_id_pairs(self) -> Dict[str, str]:
        return self.__WebSocketClient.channelid_sub_pairs

    def get_channelurl_by_name(self, channel_name: str) -> str:
        return next(key for key, val in self.__WebSocketClient.channelid_sub_pairs.items() if val == channel_name)

    def set_respond_hook(self, input_: str,
                         response: str,
                         limited_to_users: List[str] = None,
                         lower_the_input: bool = False,
                         exclude_itself: bool = True,
                         must_be_equal: bool = True,
                         limited_to_channels: List[str] = None
                         ) -> None:
        if limited_to_channels is None:
            limited_to_channels = []
        if limited_to_users is None:
            limited_to_users = []
        try:
            response.format(nickname="")
        except KeyError as e:
            raise Exception("You need to set a {nickname} key in welcome message!") from e

        def hook(resp: FrameModel) -> Optional[bool]:
            sent_message = resp.message.lower() if lower_the_input else resp.message
            if (resp.user.name in limited_to_users or not bool(limited_to_users)) \
                    and (exclude_itself and resp.user.name != self.__WebSocketClient.own_name) \
                    and ((must_be_equal and sent_message == input_) or (not must_be_equal and input_ in sent_message)) \
                    and (self.__WebSocketClient.channelid_sub_pairs.get(
                resp.channel_url) in limited_to_channels or not bool(limited_to_channels)):
                response_prepped = response.format(nickname=resp.user.name)
                self.__WebSocketClient.ws_send_message(response_prepped, resp.channel_url)
                return True

        self.event.on_message(func=hook)

    def set_welcome_message(self, message: str, limited_to_channels: List[str] = None) -> None:
        if limited_to_channels is None:
            limited_to_channels = []
        try:
            message.format(nickname="", inviter="")
        except KeyError as e:
            raise Exception("Keys should be {nickname} and {inviter}") from e

        def hook(resp: FrameModel) -> Optional[bool]:
            if self.__WebSocketClient.channelid_sub_pairs.get(resp.channel_url) in limited_to_channels or \
                    not bool(limited_to_channels):
                response_prepped = message.format(nickname=resp.data.users[0].nickname,
                                                  inviter=resp.data.users[0].inviter.nickname)
                self.__WebSocketClient.ws_send_message(response_prepped, resp.channel_url)
                return True

        self.event.on_user_joined(hook)

    def set_farewell_message(self, message: str, limited_to_channels: List[str] = None) -> None:
        if limited_to_channels is None:
            limited_to_channels = []
        try:
            message.format(nickname="")
        except KeyError as e:
            raise Exception("Key should be {nickname}") from e

        def hook(resp: FrameModel) -> Optional[bool]:
            if self.__WebSocketClient.channelid_sub_pairs.get(resp.channel_url) in limited_to_channels or \
                    not bool(limited_to_channels):
                response_prepped = message.format(nickname=resp.data.nickname)
                self.__WebSocketClient.ws_send_message(response_prepped, resp.channel_url)
                return True

        self.event.on_user_left(hook)

    def remove_event_callback(self, func: _hook) -> None:
        self.__WebSocketClient.after_message_hooks.remove(func)

    def send_message(self, text: str, channel_url: str) -> None:
        self.__WebSocketClient.ws_send_message(text, channel_url)

    def send_snoomoji(self, snoomoji: Snoo, channel_url: str) -> None:
        self.__WebSocketClient.ws_send_snoomoji(snoomoji.value, channel_url)

    def send_gif(self, gif_url: str, channel_url: str, height: int = 200, width: int = 200) -> None:
        self.__WebSocketClient.ws_send_gif(gif_url, channel_url, height, width)

    def send_img(self, img_url: str, channel_url: str, height: int = 200, width: int = 200,
                 mimetype: str = "JPEG") -> None:
        self.__WebSocketClient.ws_send_img(img_url, channel_url, height, width, mimetype)

    def send_typing_indicator(self, channel_url: str) -> None:
        self.__WebSocketClient.ws_send_typing_indicator(channel_url)

    def stop_typing_indicator(self, channel_url: str) -> None:
        self.__WebSocketClient.ws_stop_typing_indicator(channel_url)

    def run_4ever(self, auto_reconnect: bool = True, max_retries: int = 500, disable_ssl_verification: bool = False,
                  **kwargs) -> None:
        if disable_ssl_verification:
            import ssl
            sslopt = {"cert_reqs": ssl.CERT_NONE}
        else:
            sslopt = None

        self.__tools._is_running = True
        for _ in range(max_retries):
            self.__WebSocketClient.ws.run_forever(ping_interval=15, ping_timeout=5,
                                                  skip_utf8_validation=True,
                                                  sslopt=sslopt,
                                                  **kwargs,
                                                  ping_payload="{active:1}"
                                                  )
            if self.__WebSocketClient.is_logi_err and self.__r_authentication.is_reauthable:
                self.__WebSocketClient.logger.info("Re-Authenticating...")
                if self._store_session:
                    sb_access_token, _ = self._load_session(self.__r_authentication._get_repr_pkl(), force_reauth=True)
                else:
                    sb_access_token = self.__r_authentication.authenticate()['sb_access_token']
                self.__WebSocketClient.update_ws_app_urls_access_token(sb_access_token)
            elif not (
                    auto_reconnect and isinstance(self.__WebSocketClient.last_err, WebSocketConnectionClosedException)):
                break
            self.__WebSocketClient.logger.info("Auto Re-Connecting...")

    def close(self) -> None:
        self.__WebSocketClient.ws.close()

    def kick_user(self, channel_url: str, user_id: str, duration: int) -> None:
        self.__tools.kick_user(**_get_locals_without_self(locals()))

    def delete_mesg(self, channel_url: str, msg_id: int) -> None:
        self.__tools.delete_message(**_get_locals_without_self(locals()))

    def invite_user_to_channel(self, channel_url: str, nicknames: Union[str, List[str]]) -> None:
        self.__tools.invite_user(**_get_locals_without_self(locals()))

    def leave_chat(self, channel_url: str) -> None:
        self.__tools.leave_chat(**_get_locals_without_self(locals()))

    def get_chat_invites(self) -> List[Channel]:
        return self.get_channels(member_state_filter="invited_only")

    def get_channels(self, limit: int = 100, order: str = "latest_last_message", show_member: bool = True,
                     show_read_receipt: bool = True, show_empty: bool = True, member_state_filter: str = "joined_only",
                     super_mode: str = "all", public_mode: str = "all", unread_filter: str = "all",
                     hidden_mode: str = "unhidden_only", show_frozen: bool = True,
                     # custom_types: str = 'direct,group'
                     ) -> List[Channel]:
        return self.__tools.get_channels(**_get_locals_without_self(locals()))

    def get_members(self, channel_url: str, next_token: str = None, limit: int = 20,
                    order: str = "member_nickname_alphabetical", member_state_filter: str = "all",
                    nickname_startswith: str = '') -> Members:
        return self.__tools.get_members(**_get_locals_without_self(locals()))

    def get_banned_members(self, channel_url, limit: int = 100) -> BannedUsers:
        return self.__tools.get_banned_members(**_get_locals_without_self(locals()))

    def get_current_channels(self) -> List[Channel]:
        return self.__WebSocketClient.current_channels

    def get_older_messages(self, channel_url: str, message_ts: Union[int, str] = 9007199254740991,
                           custom_types: str = '*', prev_limit: int = 40, next_limit: int = 0,
                           reverse: bool = True) -> List[Message]:
        return self.__tools.get_older_messages(**_get_locals_without_self(locals()))

    def create_channel(self, nicknames: List[str], group_name: str) -> Channel:
        channel = self.__tools.create_channel(**_get_locals_without_self(locals()),
                                              own_name=self.__WebSocketClient.own_name)
        self.__WebSocketClient.add_channelid_sub_pair(channel)
        return channel

    def create_direct_channel(self, nickname: str) -> Channel:
        channel = self.__tools.create_channel(nicknames=[nickname], group_name="",
                                              own_name=self.__WebSocketClient.own_name)
        self.__WebSocketClient.add_channelid_sub_pair(channel)
        return channel

    def accept_chat_invite(self, channel_url: str) -> Channel:
        group = self.__tools.accept_chat_invite(channel_url)
        self.__WebSocketClient.update_channelid_sub_pair()
        return group

    def rename_channel(self, name: str, channel_url: str) -> Channel:
        channel = self.__tools.rename_channel(**_get_locals_without_self(locals()))
        self.__WebSocketClient.update_channelid_sub_pair()
        return channel

    def hide_chat(self, user_id: str, channel_url: str, hide_previous_messages: bool = False,
                  allow_auto_unhide: bool = True) -> None:
        self.__tools.hide_chat(**_get_locals_without_self(locals()))

    def mute_user(self, channel_url: str, user_id: str, duration: int, description: str) -> None:
        self.__tools.mute_user(**_get_locals_without_self(locals()))

    def unmute_user(self, channel_url: str, user_id: str) -> None:
        self.__tools.unmute_user(**_get_locals_without_self(locals()))

    def set_channel_frozen_status(self, channel_url: str, is_frozen: bool) -> None:
        self.__tools.set_channel_frozen_status(**_get_locals_without_self(locals()))

    def delete_channel(self, channel_url: str) -> None:
        self.__tools.delete_channel(**_get_locals_without_self(locals()))

    def send_reaction(self, reaction_icon_key: Reaction, msg_id: Union[str, int], channel_url: str) -> None:
        self.__tools.send_reaction(reaction_icon_key.value, msg_id, channel_url)

    def delete_reaction(self, reaction_icon_key: Reaction, msg_id: Union[str, int], channel_url: str) -> None:
        self.__tools.delete_reaction(reaction_icon_key.value, msg_id, channel_url)

    def enable_rate_limiter(self, max_calls: float, period: float) -> None:
        self.__WebSocketClient.RateLimiter.is_enabled = True
        self.__WebSocketClient.RateLimiter.max_calls = max_calls
        self.__WebSocketClient.RateLimiter.period = period

    def disable_rate_limiter(self) -> None:
        self.__WebSocketClient.RateLimiter.is_enabled = False

    def _load_session(self, pkl_name, force_reauth=False):
        def get_store_file_handle(pkl_name_, mode_):
            try:
                return open(f"{pkl_name_}-stored.pkl", mode_)
            except FileNotFoundError:
                return None

        session_store_f = None if force_reauth else get_store_file_handle(pkl_name, 'rb')

        if session_store_f is None or force_reauth:
            session_store_f = get_store_file_handle(pkl_name, 'wb+')
            self.__r_authentication.authenticate()
            pickle.dump(self.__r_authentication, session_store_f)
        else:
            try:
                self.__r_authentication = pickle.load(session_store_f)
            except EOFError:
                return self._load_session(pkl_name, force_reauth=True)
        session_store_f.close()

        return self.__r_authentication.sb_access_token, self.__r_authentication.user_id
