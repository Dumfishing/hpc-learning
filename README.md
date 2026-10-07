# hpc-learning

高性能计算（HPC）入门学习项目。

## 目标

把「写得出、跑得动」升级为「知道为什么快、知道怎么更快」。

## 学习计划

| 阶段 | 主题 | 关键概念 | 产出 |
|---|---|---|---|
| 1 | 工具链与计时 | 编译优化、wall clock vs CPU time | 可复现的基准测试脚本 |
| 2 | 内存层次 | 缓存行、预取、cache blocking | 分块矩阵乘法 + 加速比曲线 |
| 3 | 指令级并行 | SIMD、自动向量化报告、循环展开 | 向量化版本的 kernel |
| 4 | 多线程 | OpenMP、数据竞争、false sharing | 并行归约 |
| 5 | 性能分析 | perf、roofline、瓶颈定位 | 一份调优报告 |

## 环境

- WSL2 + Ubuntu 24.04 LTS
- gcc 13.3.0 / GNU Make 4.3
- Python 3.12（画图与分析）

## 笔记

（待补充）
