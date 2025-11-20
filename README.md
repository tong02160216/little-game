# Little Snail Goes Home 🐌

<<<<<<< HEAD
一个基于Pygame开发的像素风格迷宫冒险小游戏。玩家控制小蜗牛在迷宫中收集食物并找到回家的路。

## 项目概述

**游戏名称**: Little Snail Goes Home  
**开发语言**: Python  
**游戏框架**: Pygame  
**美术风格**: 像素风格  
**游戏类型**: 迷宫益智游戏  

---

## 游戏玩法

### 基本玩法
玩家控制小蜗牛使用 **WASD** 键在随机生成的迷宫中移动，收集食物（白菜、苹果、香蕉）并找到回家的路。每收集一个食物得1分。

### 🎯 不同得分的游戏体验

#### 得分 = 0 分
**游戏状态**: 
- ❌ 无法触发庆祝（必须收集至少1个食物）
- 即使到达房子，也不会有任何庆祝效果
- 鼓励玩家探索迷宫收集食物

**设计理念**: 防止玩家跳过收集直接通关

---

#### 得分 = 1 分 ⭐
**触发条件**: 收集1个食物后到达房子

**庆祝效果**:
- ✅ **云朵图片**: 在屏幕中央浮动（上下15像素正弦波运动）
- ✅ **Congratulations文字**: 粉色加粗文字，带8方向描边
- ✅ **庆祝音效**: celebration.mp3 播放（音量100%）
- ❌ **无气球**: 不显示彩色气球
- ❌ **无欢呼声**: 不播放欢呼音效
- ❌ **无皇冠和光束**: 未达到5分门槛

**视觉特点**: 简约而温馨的庆祝，让新手也能获得成就感

**得分显示**: 
- 位置: 屏幕底部居中
- 颜色: 白色
- 动画: 得分增加时有1.0→1.2→1.0的缩放动画

---

#### 得分 = 2-4 分 ⭐⭐
**触发条件**: 收集2-4个食物后到达房子

**庆祝效果**:
- ✅ **云朵 + Congratulations文字**（同1分）
- ✅ **庆祝音效**（同1分）
- ✅ **彩色气球**: 42个气球从屏幕底部飘起！
  - 6种不同颜色（B1-B6）
  - 每种7个，随机排列
  - 像素风格（1/3缩放）
  - 向上浮动速度3-6像素/帧
  - 左右摆动效果
- ✅ **欢呼声**: applause-cheer-236786.mp3 播放（音量80%）
- ❌ **无皇冠和光束**: 未达到5分门槛

**视觉特点**: 热闹的庆祝场景，彩色气球营造节日氛围

**得分显示**: 
- 2分: 白色
- 3分: 浅粉色 RGB(255, 200, 220)
- 4分: 浅粉色

---

#### 得分 ≥ 5 分 ⭐⭐⭐ (豪华庆祝)
**触发条件**: 收集5个或更多食物后到达房子

**庆祝效果**:
- ✅ **所有2-4分的效果**（云朵、文字、气球、欢呼声、庆祝音效）
- ✅ **金色皇冠**: 
  - 12×12像素图案
  - 三种金色渐变
  - 红宝石、蓝宝石装饰
  - 位于云朵上方，随云朵一起浮动
- ✅ **动态光束特效**: 
  - **16条光束**从皇冠向四周发射（每22.5°一条）
  - 每条光束**5段渐变**，越远越透明
  - **脉冲动画**: 正弦波扩张收缩（0.7-1.3倍动态变化）
  - **星光闪烁**: 光束末端有随机闪烁的星星
  - 金黄色 RGBA(255, 215, 0, 150)
- ✅ **持续动画**: 得分显示有1.0→1.15→1.0的循环缩放动画

**视觉特点**: 最华丽的庆祝效果，皇冠和光束彰显玩家成就

**得分显示颜色渐变**:
- 5分: 粉色 RGB(255, 182, 193)
- 6分: 粉色
- 7分: 浅红色 RGB(255, 150, 150)
- 8分: 浅红色
- 9分: 红色 RGB(255, 100, 100)
- 10分: 红色
- 11+分: 深红色 RGB(220, 50, 50)

**特殊标识**: 皇冠象征"高分王者"，光束特效如同加冕仪式

---

### 🏆 挑战模式

**10秒速通挑战**:
- 游戏开始5秒后显示: "Try if you can finish in 10s!"
- 持续显示直到游戏结束
- 鼓励玩家追求速度与效率
- 增加游戏可玩性和重复挑战性

**策略选择**:
- 🐌 稳健流: 慢慢收集所有食物，追求5分以上豪华庆祝
- ⚡ 速通流: 快速收集少量食物，挑战10秒内完成
- 🎯 完美流: 在10秒内收集5+食物并通关（终极挑战）

---

### 🎮 操作指南

#### 开始界面
1. 游戏启动后显示标题 "Little Snail Goes Home"
2. 点击绿色边框的 **START** 按钮开始游戏
3. 注意提示: "Please use English input method."（确保使用英文输入法）

#### 游戏进行中
- **W**: 向上移动
- **A**: 向左移动  
- **S**: 向下移动
- **D**: 向右移动
- **目标**: 在迷宫中收集食物（白菜🥬、苹果🍎、香蕉🍌）
- **终点**: 找到房子🏠完成游戏

#### UI提示时间轴
- **0-5秒**: 显示操作说明 "Use A W S D on keyboard to control the snail finding way home."
- **5-6秒**: 过渡期（空白）
- **6秒-结束**: 显示挑战提示 "Try if you can finish in 10s!"
- **全程**: 屏幕底部显示当前得分

#### 游戏重置
- 按 **空格键 (SPACE)** 可以重置游戏
- 重新生成迷宫
- 清空得分
- 重新开始计时

---

### 🎨 视觉系统详解

#### 像素艺术风格
游戏所有元素均采用统一的像素艺术风格，营造复古游戏氛围：

**文字像素化**:
- 使用方块字体（Courier New, Consolas, Monaco等）
- 小字号渲染后放大2-3.5倍
- 创造经典像素游戏质感

**图片像素化**:
- 气球: 1/3缩放创建像素块效果
- 云朵: 1/8缩放 + smoothscale平滑处理
- 所有游戏元素保持统一美学

**UI像素化**:
- 按钮边框: 8×8像素方块拼接
- 文字背景: 白色填充 + 灰色像素边框
- START按钮: 深绿色边框线装饰

#### 动画系统
- **云朵浮动**: 正弦波上下运动，周期性15像素
- **气球上升**: 线性向上 + 左右摆动
- **得分缩放**: 12帧动画，增分时放大1.2倍
- **光束脉冲**: 正弦波扩张，0.7-1.3倍动态变化
- **星光闪烁**: 随机透明度，营造闪烁效果

#### 颜色设计
- **背景**: 天蓝色 RGB(135, 206, 235)
- **得分文字**: 6级颜色渐变（白→粉→红）
- **皇冠**: 金色三段渐变 + 宝石点缀
- **光束**: 金黄色半透明 RGBA(255, 215, 0, 150)

---

## 技术实现

### 核心技术栈
- **Python 3.x**
- **Pygame 2.x**: 游戏框架
  - `pygame.transform`: 图像缩放、像素化处理
  - `pygame.font`: 字体渲染、像素文字
  - `pygame.draw`: 图形绘制 (矩形、线条)
  - `pygame.mixer`: 音频播放管理
  - `pygame.time`: 时间控制、动画计时

### 分级奖励机制实现

```python
# 得分0: 不触发庆祝
if player_x == end_x and player_y == end_y and score > 0:
    celebration_started = True

# 得分1: 基础庆祝（云朵+文字+音效）
if celebration_started:
    # 播放庆祝音效
    celebration_sound.play()
    # 绘制云朵和Congratulations文字

# 得分>1: 完整庆祝（+气球+欢呼声）
if celebration_started and score > 1:
    # 创建42个彩色气球
    for balloon_img in balloon_images:
        for _ in range(7):
            celebration_balloons.append(CelebrationBalloon(balloon_img))
    # 播放欢呼声
    applause_sound.play()

# 得分≥5: 豪华庆祝（+皇冠+光束）
if celebration_started and score >= 5:
    # 绘制皇冠
    draw_crown(screen, crown_x, crown_y)
    # 绘制16条动态光束
=======
A pixel-art style maze adventure game developed with Pygame. Players control a little snail to collect food in a maze and find the way home.

## Project Overview

**Game Name**: Little Snail Goes Home  
**Development Language**: Python  
**Game Framework**: Pygame  
**Art Style**: Pixel Art  
**Game Type**: Maze Puzzle Game  

---

## Gameplay

### Basic Gameplay
Players control the little snail using **WASD** keys to move through randomly generated mazes, collect food (cabbage, apple, banana), and find the way home. Each food item collected earns 1 point.

### 🎯 Game Experience at Different Scores

#### Score = 0 Points
**Game State**: 
- ❌ Cannot trigger celebration (must collect at least 1 food item)
- No celebration effects even when reaching the house
- Encourages players to explore the maze and collect food

**Design Philosophy**: Prevents players from skipping collection and going straight to the finish

---

#### Score = 1 Point ⭐
**Trigger Condition**: Collect 1 food item and reach the house

**Celebration Effects**:
- ✅ **Cloud Image**: Floating at screen center (sinusoidal vertical motion of ±15 pixels)
- ✅ **Congratulations Text**: Pink bold text with 8-direction outline
- ✅ **Celebration Sound**: celebration.mp3 plays (100% volume)
- ❌ **No Balloons**: Colorful balloons not displayed
- ❌ **No Cheering**: Applause sound not played
- ❌ **No Crown & Beams**: Hasn't reached 5-point threshold

**Visual Characteristics**: Simple yet warm celebration, giving beginners a sense of achievement

**Score Display**: 
- Position: Bottom center of screen
- Color: White
- Animation: 1.0→1.2→1.0 scaling animation when score increases

---

#### Score = 2-4 Points ⭐⭐
**Trigger Condition**: Collect 2-4 food items and reach the house

**Celebration Effects**:
- ✅ **Cloud + Congratulations Text** (same as 1 point)
- ✅ **Celebration Sound** (same as 1 point)
- ✅ **Colorful Balloons**: 42 balloons floating up from bottom of screen!
  - 6 different colors (B1-B6)
  - 7 of each, randomly arranged
  - Pixel style (1/3 scale)
  - Rising speed 3-6 pixels/frame
  - Left-right swaying effect
- ✅ **Cheering Sound**: applause-cheer-236786.mp3 plays (80% volume)
- ❌ **No Crown & Beams**: Hasn't reached 5-point threshold

**Visual Characteristics**: Lively celebration scene, colorful balloons create festive atmosphere

**Score Display**: 
- 2 points: White
- 3 points: Light pink RGB(255, 200, 220)
- 4 points: Light pink

---

#### Score ≥ 5 Points ⭐⭐⭐ (Luxury Celebration)
**Trigger Condition**: Collect 5 or more food items and reach the house

**Celebration Effects**:
- ✅ **All 2-4 Point Effects** (cloud, text, balloons, cheering, celebration sound)
- ✅ **Golden Crown**: 
  - 12×12 pixel pattern
  - Three shades of gold gradient
  - Ruby and sapphire decorations
  - Positioned above cloud, floating with cloud
- ✅ **Dynamic Beam Effects**: 
  - **16 beams** radiating from crown in all directions (every 22.5°)
  - Each beam has **5 gradient segments**, increasingly transparent outward
  - **Pulse animation**: Sinusoidal expansion/contraction (0.7-1.3x dynamic variation)
  - **Starlight sparkles**: Randomly flickering stars at beam endpoints
  - Golden color RGBA(255, 215, 0, 150)
- ✅ **Continuous Animation**: Score display has 1.0→1.15→1.0 looping scaling animation

**Visual Characteristics**: Most magnificent celebration effect, crown and beams showcase player achievement

**Score Display Color Gradient**:
- 5 points: Pink RGB(255, 182, 193)
- 6 points: Pink
- 7 points: Light red RGB(255, 150, 150)
- 8 points: Light red
- 9 points: Red RGB(255, 100, 100)
- 10 points: Red
- 11+ points: Deep red RGB(220, 50, 50)

**Special Badge**: Crown symbolizes "High Score King", beam effects like a coronation ceremony

---

### 🏆 Challenge Mode

**10-Second Speedrun Challenge**:
- Appears 5 seconds after game starts: "Try if you can finish in 10s!"
- Displays continuously until game ends
- Encourages players to pursue speed and efficiency
- Increases game replayability and challenge

**Strategy Choices**:
- 🐌 Steady Mode: Slowly collect all food, aim for 5+ points luxury celebration
- ⚡ Speedrun Mode: Quickly collect minimal food, challenge 10-second completion
- 🎯 Perfect Mode: Collect 5+ food and finish within 10 seconds (ultimate challenge)

---

### 🎮 Control Guide

#### Start Screen
1. Game displays title "Little Snail Goes Home" on startup
2. Click green-bordered **START** button to begin game
3. Note the reminder: "Please use English input method." (ensure English input mode)

#### During Gameplay
- **W**: Move up
- **A**: Move left  
- **S**: Move down
- **D**: Move right
- **Goal**: Collect food in the maze (cabbage🥬, apple🍎, banana🍌)
- **Finish**: Find the house🏠 to complete the game

#### UI Prompt Timeline
- **0-5 seconds**: Display controls "Use A W S D on keyboard to control the snail finding way home."
- **5-6 seconds**: Transition period (blank)
- **6 seconds-end**: Display challenge prompt "Try if you can finish in 10s!"
- **Throughout**: Current score displayed at bottom of screen

#### Game Reset
- Press **SPACE** to reset game
- Regenerate maze
- Clear score
- Restart timer

---

### 🎨 Visual System Details

#### Pixel Art Style
All game elements use unified pixel art style, creating retro gaming atmosphere:

**Text Pixelation**:
- Use square fonts (Courier New, Consolas, Monaco, etc.)
- Render at small size then scale up 2-3.5x
- Creates classic pixel game texture

**Image Pixelation**:
- Balloons: 1/3 scale creates pixel block effect
- Cloud: 1/8 scale + smoothscale for smooth processing
- All game elements maintain unified aesthetics

**UI Pixelation**:
- Button borders: 8×8 pixel blocks stitched together
- Text backgrounds: White fill + gray pixel border
- START button: Dark green border decoration

#### Animation System
- **Cloud Floating**: Sinusoidal vertical motion, periodic 15-pixel movement
- **Balloon Rising**: Linear upward + left-right swaying
- **Score Scaling**: 12-frame animation, 1.2x enlargement on score gain
- **Beam Pulse**: Sinusoidal expansion, 0.7-1.3x dynamic scaling
- **Starlight Flicker**: Random opacity variation creating twinkling effect

#### Color Design
- **Background**: Sky blue RGB(135, 206, 235)
- **Score Text**: 6-level color gradient (white→pink→red)
- **Crown**: Gold three-tone gradient + gem accents
- **Beams**: Golden semi-transparent RGBA(255, 215, 0, 150)

---

## Technical Implementation

### Core Technology Stack
- **Python 3.x**
- **Pygame 2.x**: Game framework
  - `pygame.transform`: Image scaling, pixelation processing
  - `pygame.font`: Font rendering, pixel text
  - `pygame.draw`: Graphics drawing (rectangles, lines)
  - `pygame.mixer`: Audio playback management
  - `pygame.time`: Time control, animation timing

### Tiered Reward Mechanism Implementation

```python
# Score 0: No celebration triggered
if player_x == end_x and player_y == end_y and score > 0:
    celebration_started = True

# Score 1: Basic celebration (cloud+text+sound)
if celebration_started:
    # Play celebration sound
    celebration_sound.play()
    # Draw cloud and Congratulations text

# Score >1: Full celebration (+balloons+cheering)
if celebration_started and score > 1:
    # Create 42 colorful balloons
    for balloon_img in balloon_images:
        for _ in range(7):
            celebration_balloons.append(CelebrationBalloon(balloon_img))
    # Play cheering sound
    applause_sound.play()

# Score ≥5: Luxury celebration (+crown+beams)
if celebration_started and score >= 5:
    # Draw crown
    draw_crown(screen, crown_x, crown_y)
    # Draw 16 dynamic beams
>>>>>>> a0961f32532dbcbf4f5cfbe2b890a677834c668d
    for angle in range(16):
        draw_beam(screen, angle * 22.5, pulse_animation)
```

<<<<<<< HEAD
### 核心算法

**1. 迷宫生成**:
- 随机生成算法
- 路径验证确保可达性

**2. 碰撞检测**:
- 基于网格的位置检测
- 食物收集判定
- 房子到达判定

**3. 像素化渲染**:
```python
# 缩小再放大创建像素效果
=======
### Core Algorithms

**1. Maze Generation**:
- Random generation algorithm
- Path validation ensures reachability

**2. Collision Detection**:
- Grid-based position detection
- Food collection detection
- House arrival detection

**3. Pixelation Rendering**:
```python
# Scale down then up to create pixel effect
>>>>>>> a0961f32532dbcbf4f5cfbe2b890a677834c668d
small_surface = font.render(text, True, color)
pixel_surface = pygame.transform.scale(small_surface, (width * scale, height * scale))
```

<<<<<<< HEAD
**4. 动画插值**:
```python
# 正弦波动画
offset = math.sin(angle) * amplitude
# 脉冲动画
pulse = math.sin(frame * speed + offset) * range + base
```

**5. 颜色渐变**:
```python
# 基于分数的颜色插值
=======
**4. Animation Interpolation**:
```python
# Sinusoidal wave animation
offset = math.sin(angle) * amplitude
# Pulse animation
pulse = math.sin(frame * speed + offset) * range + base
```

**5. Color Gradient**:
```python
# Score-based color interpolation
>>>>>>> a0961f32532dbcbf4f5cfbe2b890a677834c668d
if score >= threshold:
    color = lerp(color1, color2, factor)
```

<<<<<<< HEAD
### 代码结构
- **主文件**: `import pygame.py` (~1218行)
- **主要类**:
  - `CelebrationBalloon`: 庆祝气球类
- **主要函数**:
  - `generate_maze()`: 迷宫生成
  - `draw_maze()`: 迷宫绘制
  - `draw_crown()`: 皇冠绘制
- **游戏循环**:
  - 开始界面循环
  - 主游戏循环

---

## 游戏特色

### 1. 三级分级奖励系统 🎁
根据玩家得分提供三个层次的庆祝效果：
- **1分**: 温馨基础庆祝，让新手也有成就感
- **2-4分**: 热闹完整庆祝，彩色气球营造节日氛围
- **5+分**: 豪华加冕仪式，皇冠和光束彰显高分王者

这种设计让每个分数段都有独特的视觉反馈，激励玩家不断挑战更高分数。

### 2. 精致的像素艺术风格 🎨
- 统一的视觉语言
- 复古游戏美学
- 所有元素均采用像素化处理
- 从文字、UI到游戏对象完全统一

### 3. 丰富的视觉反馈 ✨
- 多层次庆祝动画（云朵、气球、皇冠、光束）
- 得分颜色渐变（6级颜色）
- 动态光效系统（16条脉冲光束）
- 平滑的动画过渡（30 FPS稳定运行）

### 4. 用户体验优化 👍
- 分阶段显示指令（避免信息过载）
  - 先教操作（5秒）
  - 再提挑战（持续到结束）
- 鼠标悬停效果（START按钮）
- 视觉和听觉双重反馈
- 明确的操作提示和输入法提醒

### 5. 灵活的游戏节奏 ⚡
- **休闲模式**: 慢慢探索，收集所有食物
- **速通模式**: 10秒挑战，追求效率
- **完美模式**: 高分+速通双重挑战
- 按空格键随时重置，重复挑战

---

## 工作量统计

### 开发阶段

#### 第一阶段: 基础游戏框架
- 迷宫生成系统
- 玩家移动控制
- 食物收集机制
- 基础UI显示

#### 第二阶段: 像素风格改造
- 所有气球像素化 (1/3缩放)
- 云朵像素化 (1/8缩放 + smoothscale)
- 文字像素化 (多级别放大)
- 按钮像素化 (方块边框)

#### 第三阶段: 庆祝系统开发
- 庆祝触发逻辑
- 气球类实现 (浮动、摆动动画)
- 云朵浮动动画
- Congratulations文字渲染 (描边效果)
- 庆祝状态锁定机制

#### 第四阶段: 音效系统集成
- 背景音乐加载播放
- 庆祝音效
- 欢呼声音效
- 食物收集音效
- 音量平衡调整

#### 第五阶段: 高级视觉特效
- 皇冠绘制系统 (12×12像素图案)
- 16方向光束系统
- 光束动态脉冲动画
- 5段渐变透明度
- 星光闪烁效果

#### 第六阶段: 得分系统优化
- 得分显示重新定位 (底部居中)
- 得分颜色渐变系统 (6级颜色)
- 双重动画系统 (得分时 + 持续循环)
- 描边效果增强可读性

#### 第七阶段: 开始界面完善
- 游戏标题设计
- START按钮交互
- 输入法提示
- 像素风格统一
- 深绿色边框装饰

#### 第八阶段: UI文字系统
- 玩法说明渲染
- 时间控制系统 (5秒显示)
- 挑战文字添加 (10秒提示)
- 分阶段显示逻辑
- 白色背景 + 边框设计

#### 第九阶段: 游戏逻辑优化
- 庆祝条件优化 (score > 0)
- 分级奖励机制 (score > 1 判断)
- 空格键重置完善
- 时间计时器重置
- 状态管理优化

#### 第十阶段: 细节打磨
- 所有文字像素化统一
- 动画同步优化
- 性能优化 (30 FPS稳定)
- 边缘情况处理
- 视觉层级调整

---

## 技术亮点

### 1. 像素艺术渲染引擎
自研像素化渲染系统，通过缩放算法实现统一的像素美学。

### 2. 多层动画系统
独立的动画计时器，支持多个动画同时运行且不互相干扰。

### 3. 动态光效算法
基于三角函数的光束系统，16方向同步脉冲动画。

### 4. 状态机管理
清晰的游戏状态管理 (开始界面 → 游戏中 → 庆祝状态 → 重置)。

### 5. 分级反馈机制
根据玩家表现提供不同层次的视觉和听觉奖励。

---

## 运行要求

### 环境
- Python 3.7+
- Pygame 2.0+

### 安装依赖
=======
### Code Structure
- **Main File**: `import pygame.py` (~1218 lines)
- **Main Classes**:
  - `CelebrationBalloon`: Celebration balloon class
- **Main Functions**:
  - `generate_maze()`: Maze generation
  - `draw_maze()`: Maze rendering
  - `draw_crown()`: Crown rendering
- **Game Loops**:
  - Start screen loop
  - Main game loop

---

## Game Features

### 1. Three-Tier Reward System 🎁
Provides three levels of celebration effects based on player score:
- **1 point**: Warm basic celebration, gives beginners sense of achievement
- **2-4 points**: Lively full celebration, colorful balloons create festive atmosphere
- **5+ points**: Luxury coronation ceremony, crown and beams showcase high score mastery

This design ensures each score range has unique visual feedback, motivating players to challenge higher scores.

### 2. Exquisite Pixel Art Style 🎨
- Unified visual language
- Retro gaming aesthetics
- All elements pixelated
- Complete consistency from text, UI to game objects

### 3. Rich Visual Feedback ✨
- Multi-layered celebration animations (cloud, balloons, crown, beams)
- Score color gradient (6 levels)
- Dynamic lighting system (16 pulsing beams)
- Smooth animation transitions (stable 30 FPS)

### 4. User Experience Optimization 👍
- Staged instruction display (avoids information overload)
  - First teach controls (5 seconds)
  - Then present challenge (until end)
- Mouse hover effects (START button)
- Visual and audio dual feedback
- Clear operation prompts and input method reminders

### 5. Flexible Game Pace ⚡
- **Casual Mode**: Slowly explore, collect all food
- **Speedrun Mode**: 10-second challenge, pursue efficiency
- **Perfect Mode**: High score + speedrun dual challenge
- Press SPACE anytime to reset, repeat challenges

---

## Work Summary

### Development Phases

#### Phase 1: Basic Game Framework
- Maze generation system
- Player movement control
- Food collection mechanics
- Basic UI display

#### Phase 2: Pixel Style Transformation
- All balloon pixelation (1/3 scale)
- Cloud pixelation (1/8 scale + smoothscale)
- Text pixelation (multi-level scaling)
- Button pixelation (block borders)

#### Phase 3: Celebration System Development
- Celebration trigger logic
- Balloon class implementation (floating, swaying animation)
- Cloud floating animation
- Congratulations text rendering (outline effect)
- Celebration state locking mechanism

#### Phase 4: Sound System Integration
- Background music loading and playback
- Celebration sound effects
- Cheering sound effects
- Food collection sound effects
- Volume balance adjustment

#### Phase 5: Advanced Visual Effects
- Crown rendering system (12×12 pixel pattern)
- 16-direction beam system
- Beam dynamic pulse animation
- 5-segment gradient transparency
- Starlight flicker effects

#### Phase 6: Score System Optimization
- Score display repositioning (bottom center)
- Score color gradient system (6 color levels)
- Dual animation system (on score + continuous loop)
- Outline effect enhances readability

#### Phase 7: Start Screen Enhancement
- Game title design
- START button interaction
- Input method reminder
- Unified pixel style
- Dark green border decoration

#### Phase 8: UI Text System
- Gameplay instruction rendering
- Time control system (5-second display)
- Challenge text addition (10-second prompt)
- Staged display logic
- White background + border design

#### Phase 9: Game Logic Optimization
- Celebration condition optimization (score > 0)
- Tiered reward mechanism (score > 1 judgment)
- SPACE key reset refinement
- Timer reset
- State management optimization

#### Phase 10: Detail Polish
- Unified text pixelation
- Animation synchronization optimization
- Performance optimization (stable 30 FPS)
- Edge case handling
- Visual hierarchy adjustment

---

## Technical Highlights

### 1. Pixel Art Rendering Engine
Self-developed pixelation rendering system achieving unified pixel aesthetics through scaling algorithms.

### 2. Multi-Layer Animation System
Independent animation timers supporting multiple simultaneous animations without interference.

### 3. Dynamic Lighting Algorithm
Trigonometry-based beam system with 16-direction synchronized pulse animation.

### 4. State Machine Management
Clear game state management (start screen → in-game → celebration → reset).

### 5. Tiered Feedback Mechanism
Different levels of visual and audio rewards based on player performance.

---

## System Requirements

### Environment
- Python 3.7+
- Pygame 2.0+

### Install Dependencies
>>>>>>> a0961f32532dbcbf4f5cfbe2b890a677834c668d
```bash
pip install pygame
```

<<<<<<< HEAD
### 运行游戏
=======
### Run Game
>>>>>>> a0961f32532dbcbf4f5cfbe2b890a677834c668d
```bash
python "import pygame.py"
```

<<<<<<< HEAD
### 资源文件
确保以下资源文件位于 `F:/code/little_game/` 目录:
- **图片**: 云.png, 房子3.png, B1-B6.png, 食物图片, 玩家图片
- **音频**: celebration.mp3, applause-cheer-236786.mp3, shine-11-268907.mp3, 背景音乐

---

## 快速开始

### 第一次游玩建议

**新手路线**（熟悉游戏）:
1. 点击START按钮开始
2. 仔细阅读操作说明（前5秒）
3. 先收集1-2个食物，看看基础庆祝效果
4. 按空格键重置，尝试收集更多食物

**进阶路线**（挑战高分）:
1. 尝试收集5个以上食物
2. 解锁皇冠和光束特效
3. 观察得分颜色的渐变变化
4. 体验最华丽的庆祝效果

**速通路线**（10秒挑战）:
1. 注意第6秒出现的挑战提示
2. 规划最短路径
3. 快速收集1-2个食物即可通关
4. 挑战在10秒内完成游戏

**完美路线**（终极挑战）:
1. 10秒内收集5个以上食物
2. 需要对迷宫布局有很好的判断
3. 完成后可以看到豪华庆祝效果
4. 这是最高难度的玩法！

---

## 游戏流程

1. 启动游戏 → 显示开始界面
2. 点击START按钮 → 进入游戏
3. 查看操作说明 (5秒) → 10秒挑战提示出现 (6秒后)
4. 使用WASD控制蜗牛移动
5. 收集食物增加分数
6. 到达房子触发庆祝
   - 1分: 简约温馨
   - 2-4分: 热闹欢快
   - 5+分: 豪华加冕
7. 按空格键重新开始，尝试不同玩法

---

## 资源文件清单

### 图片资源 (F:/code/little_game/)
| 文件名 | 用途 | 规格 |
|--------|------|------|
| 云.png | 庆祝背景云朵 | 868×337像素 |
| 房子3.png | 终点房子 | - |
| B1.png | 红色气球 | - |
| B2.png | 橙色气球 | - |
| B3.png | 黄色气球 | - |
| B4.png | 绿色气球 | - |
| B5.png | 蓝色气球 | - |
| B6.png | 紫色气球 | - |
| 白菜/苹果/香蕉图片 | 可收集食物 | - |
| 蜗牛图片 | 玩家角色 | - |

### 音频资源 (F:/code/little_game/)
| 文件名 | 用途 | 音量 | 触发条件 |
|--------|------|------|----------|
| celebration.mp3/wav | 庆祝音效 | 100% | 所有得分 |
| applause-cheer-236786.mp3 | 欢呼声 | 80% | 得分>1 |
| shine-11-268907.mp3 | 收集食物音效 | 60% | 吃食物时 |
| 背景音乐文件 | 游戏BGM | - | 游戏全程 |

---

## 控制说明

| 按键 | 功能 |
|------|------|
| W | 向上移动 |
| A | 向左移动 |
| S | 向下移动 |
| D | 向右移动 |
| SPACE | 重置游戏（重新生成迷宫） |
| 鼠标左键 | 点击START按钮开始游戏 |

---

## 开发总结

本项目是一个功能完整、视觉精美的像素风格迷宫游戏。通过精心设计的动画系统、分级奖励机制和统一的像素美学，为玩家提供了优秀的游戏体验。

### 代码行数
- 主程序: ~1218行 Python代码

### 开发周期
- 持续迭代优化
- 10个主要开发阶段
- 多次细节打磨

### 主要成就
✅ 完整的游戏循环  
✅ 统一的像素艺术风格  
✅ 丰富的动画效果  
✅ 完善的音效系统  
✅ 多层次奖励机制  
✅ 流畅的用户体验  
✅ 清晰的代码结构  

---

## 作者

tong02160216

## 版本

1.0.0

## 许可证

MIT License

---

**享受游戏吧！🎮✨**
=======
### Resource Files
Ensure the following resource files are in `F:/code/little_game/` directory:
- **Images**: 云.png, 房子3.png, B1-B6.png, food images, player images
- **Audio**: celebration.mp3, applause-cheer-236786.mp3, shine-11-268907.mp3, background music

---

## Quick Start

### First-Time Play Recommendations

**Beginner Route** (Familiarize with game):
1. Click START button to begin
2. Carefully read control instructions (first 5 seconds)
3. First collect 1-2 food items to see basic celebration
4. Press SPACE to reset, try collecting more food

**Advanced Route** (Challenge high score):
1. Try collecting 5 or more food items
2. Unlock crown and beam effects
3. Observe score color gradient changes
4. Experience the most magnificent celebration

**Speedrun Route** (10-second challenge):
1. Watch for challenge prompt appearing at 6 seconds
2. Plan shortest path
3. Quickly collect 1-2 food items to finish
4. Challenge completing game within 10 seconds

**Perfect Route** (Ultimate challenge):
1. Collect 5+ food items within 10 seconds
2. Requires excellent maze layout judgment
3. Can see luxury celebration upon completion
4. This is the highest difficulty gameplay!

---

## Game Flow

1. Launch game → Display start screen
2. Click START button → Enter game
3. View controls (5 sec) → 10-second challenge prompt appears (after 6 sec)
4. Use WASD to control snail movement
5. Collect food to increase score
6. Reach house to trigger celebration
   - 1 point: Simple and warm
   - 2-4 points: Lively and cheerful
   - 5+ points: Luxury coronation
7. Press SPACE to restart, try different playstyles

---

## Resource File List

### Image Resources (F:/code/little_game/)
| Filename | Purpose | Specs |
|----------|---------|-------|
| 云.png | Celebration background cloud | 868×337 pixels |
| 房子3.png | Finish line house | - |
| B1.png | Red balloon | - |
| B2.png | Orange balloon | - |
| B3.png | Yellow balloon | - |
| B4.png | Green balloon | - |
| B5.png | Blue balloon | - |
| B6.png | Purple balloon | - |
| Cabbage/Apple/Banana images | Collectible food | - |
| Snail image | Player character | - |

### Audio Resources (F:/code/little_game/)
| Filename | Purpose | Volume | Trigger Condition |
|----------|---------|--------|-------------------|
| celebration.mp3/wav | Celebration sound | 100% | All scores |
| applause-cheer-236786.mp3 | Cheering sound | 80% | Score > 1 |
| shine-11-268907.mp3 | Food collection sound | 60% | When eating food |
| Background music file | Game BGM | - | Throughout game |

---

## Controls

| Key | Function |
|-----|----------|
| W | Move up |
| A | Move left |
| S | Move down |
| D | Move right |
| SPACE | Reset game (regenerate maze) |
| Left Mouse Click | Click START button to begin game |

---

## Development Summary

This project is a fully-functional, visually stunning pixel-style maze game. Through carefully designed animation systems, tiered reward mechanisms, and unified pixel aesthetics, it provides excellent gaming experience for players.

### Lines of Code
- Main program: ~1218 lines of Python code

### Development Cycle
- Continuous iterative optimization
- 10 major development phases
- Multiple detail polishing sessions

### Main Achievements
✅ Complete game loop  
✅ Unified pixel art style  
✅ Rich animation effects  
✅ Comprehensive sound system  
✅ Multi-tier reward mechanism  
✅ Smooth user experience  
✅ Clear code structure  

---

## Author

tong02160216

## Version

1.0.0

## License

MIT License


https://github.com/user-attachments/assets/26e7e8cc-b9e7-4621-b5d6-c113c3142a86




---

**Enjoy the game! 🎮✨**
>>>>>>> a0961f32532dbcbf4f5cfbe2b890a677834c668d
