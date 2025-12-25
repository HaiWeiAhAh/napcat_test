# -*- coding: utf-8 -*-
import asyncio
import sys
import json
import websockets as Server


async def napcat_server():
    print("正在启动adapter...")
    async with Server.serve(message_recv,"0.0.0.0",9099) as server:
        print(
            f"Adapter已启动，监听地址: ws://0.0.0.0:9000"
        )
        await server.serve_forever()

async def message_recv(server_connection: Server.ServerConnection):
    async for raw_message in server_connection:
        print(
            f"{raw_message[:100]}..."
            if (len(raw_message) > 100)
            else raw_message
        )
        decoded_raw_message: dict = json.loads(raw_message)
        post_type = decoded_raw_message.get("post_type")
        if post_type in ["meta_event", "message", "notice"]:
            print(decoded_raw_message)
        elif post_type is None:
            print(decoded_raw_message)

async def shutdown():
    try:
        print("正在关闭adapter...")
        tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]
        for task in tasks:
            if not task.done():
                task.cancel()
        await asyncio.wait_for(asyncio.gather(*tasks, return_exceptions=True), 15)
        print("Adapter已成功关闭")
    except Exception as e:
        print(f"Adapter关闭中出现错误: {e}")

async def main():
    await asyncio.gather(napcat_server())

if __name__ == '__main__':
    loop = asyncio.new_event_loop()  # 1. 显式创建新的事件循环
    asyncio.set_event_loop(loop)  # 2. 将新循环设为当前线程的默认循环
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        print("信号中断正在关闭")
        loop.run_until_complete(shutdown())
    except Exception as e:
        print(e)
        sys.exit(1)
    finally:
        if loop and not loop.is_closed():
            loop.close()
        sys.exit(0)