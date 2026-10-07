"""ProMentor 自检文件：确认工具链可用。

也可以当作这个项目的第一段可运行代码 —— README 里「怎样运行项目」正好需要它。
"""
import platform
import subprocess
import sys


def version(cmd):
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        return (out.stdout or out.stderr).strip().splitlines()[0]
    except Exception as exc:
        return f"不可用 ({exc})"


def main():
    print("hpc-learning 环境自检")
    print("=" * 40)
    print(f"Python  : {sys.version.split()[0]}")
    print(f"平台    : {platform.system()} {platform.release()}")
    print(f"架构    : {platform.machine()}")
    print(f"CPU 核数: {platform.os.cpu_count() if hasattr(platform, 'os') else 'n/a'}")
    print(f"gcc     : {version(['gcc', '--version'])}")
    print(f"git     : {version(['git', '--version'])}")
    print("=" * 40)
    print("如果上面都打印出来了，说明工具链已接通。")


if __name__ == "__main__":
    main()
