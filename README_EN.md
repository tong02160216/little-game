# Little Snail Goes Home 🐌

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
    for angle in range(16):
        draw_beam(screen, angle * 22.5, pulse_animation)
```

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
small_surface = font.render(text, True, color)
pixel_surface = pygame.transform.scale(small_surface, (width * scale, height * scale))
```

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
if score >= threshold:
    color = lerp(color1, color2, factor)
```

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
```bash
pip install pygame
```

### Run Game
```bash
python "import pygame.py"
```

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

---

**Enjoy the game! 🎮✨**
