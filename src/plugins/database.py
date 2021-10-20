import aiosqlite
import sqlite3
import asyncio
import nonebot

driver: nonebot.Driver = nonebot.get_driver()
config: nonebot.config.Config = driver.config


@driver.on_startup
async def init_db():
    config.db = await aiosqlite.connect("src/static/Kiba.db")
    try:
        await config.db.executescript(
            "create table group_poke_table (group_id bigint primary key not null, last_trigger_time int, triggered int, disabled bit, strategy text);"
            "create table user_poke_table (user_id bigint, group_id bigint, triggered int);"
            "create table waiting_table (group_id bigint, shop text, waiting int);"
            )
    except Exception:
        pass

@driver.on_shutdown
async def free_db():
    await config.db.close()