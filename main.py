from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from astrbot.api import logger, AstrBotConfig
from astrbot.core.message.components import Reply


@register(
    "astrbot_plugin_smart_quote",
    "Nick",
    "群聊 / 私聊独立控制是否引用消息",
    "1.0.0",
)
class SmartQuotePlugin(Star):
    def __init__(self, context: Context, config: AstrBotConfig):
        super().__init__(context)
        self.config = config
        self.quote_in_group = config.get("quote_in_group", True)
        self.quote_in_private = config.get("quote_in_private", False)

    async def initialize(self):
        logger.info(
            "[SmartQuote] Loaded | "
            f"group={self.quote_in_group} "
            f"private={self.quote_in_private}"
        )

    @filter.on_decorating_result(priority=10)
    async def control_quote(self, event: AstrMessageEvent):
        result = event.get_result()
        if not result or not result.chain:
            return

        is_group = bool(event.message_obj.group_id)
        need_quote = self.quote_in_group if is_group else self.quote_in_private

        if not need_quote:
            return

        msg_id = event.message_obj.message_id
        if not msg_id:
            return

        # 防止重复插 Reply
        if isinstance(result.chain[0], Reply):
            return

        result.chain.insert(0, Reply(id=msg_id))

        logger.debug(
            f"[SmartQuote] "
            f"{'GROUP' if is_group else 'PRIVATE'} "
            f"insert Reply({msg_id})"
        )
