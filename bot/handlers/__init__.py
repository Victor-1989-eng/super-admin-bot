from aiogram import Router

from bot.handlers.antispam import router as antispam_router
from bot.handlers.basic import router as basic_router
from bot.handlers.moderation import router as moderation_router
from bot.handlers.panel import router as panel_router
from bot.handlers.stats import router as stats_router
from bot.handlers.welcome import router as welcome_router

router = Router()

router.include_router(basic_router)
router.include_router(welcome_router)
router.include_router(panel_router)
router.include_router(moderation_router)
router.include_router(antispam_router)
router.include_router(stats_router)
