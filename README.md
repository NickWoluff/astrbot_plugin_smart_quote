# 智能引用信息
<img src="logo.png" width="32" height="32" />

[![License](https://img.shields.io/badge/license-AGPL--3.0-blue?style=flat-square)](./LICENSE)

## 简介

**Smart Quote Plugin** 是一个为 **AstrBot** 设计的智能消息引用控制插件，用于解决 AstrBot 原生配置中  
**“回复时引用发送人消息（reply_with_quote）只能全局开启或关闭”** 的问题。

通过本插件，可以实现：

- **独立控制群聊与私聊时的回复是否引用发送人消息（请先禁用官方自带的“Astrbot-配置文件-平台配置-回复时引用发送人消息”）**

插件基于 AstrBot 的事件系统实现，**无需修改核心代码**，即插即用。

> 作者：尼克狼唔 `Nick Woluff`


## 功能特点

- **群聊 / 私聊分离控制**
  - 群聊可启用引用，避免多用户环境下回复混乱
  - 私聊默认关闭引用，聊天更自然
- **事件后处理机制**
  - 在消息发送前动态决定是否附带 Reply
- **无侵入设计**
  - 不修改 AstrBot Core
  - 与其他插件高度兼容
- **配置简单**
  - 支持通过配置文件灵活控制行为

## 系统要求

- **AstrBot**（支持 `Star` 插件机制）
- **Python 3.8 及以上**
- 已正常运行的 AstrBot 环境

## 安装方法

- 直接在Astrbot插件市场安装即可

## 发布说明

- 本项目基于 [**GNU Affero General Public License v3.0 (AGPL-3.0)**](./LICENSE) 开源
- 仅用于学习用途免费分享，勿用于商业分发
- 若需反馈问题或建议，请在 Issues 中留言


## 版权信息

> Copyright © 2026 Nick Woluff. All Rights Reserved.
