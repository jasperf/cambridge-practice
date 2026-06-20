# Python Platformer Game Course — Curriculum Plan

**Course Type:** Interactive Self-Marking Worksheets + Guided Projects  
**Target:** Student with Python basics (variables, loops, functions, lists)  
**Goal:** Build a 2-level Mario/Prince of Persia style platformer  
**Library:** Arcade (simpler API than Pygame, same capabilities)  
**Format:** Browser-based worksheets + Mac coding projects

---

## 🎯 Course Overview

This course teaches game development with Python's **Arcade library** through a combination of:

1. **In-Browser Worksheets** (`python/` folder) — Interactive, self-checking exercises
   - Code tracing questions ("What does this print?")
   - Debugging challenges ("Fix the bug")
   - Concept quizzes (MCQ, multi-select)
   - Interactive visualizations (SVG-based, like circuits.html)
   - Instant feedback with hints and answers

2. **Guided Project Sheets** (`python/platformer/` folder) — Step-by-step game building
   - Each sheet = one game feature milestone
   - Clear instructions with code snippets
   - Checkpoints: "Test your code does X"
   - Common errors and fixes
   - Self-assessment questions (auto-checked in browser)
   - Student codes on their Mac, worksheet guides in browser

---

## 📁 Folder Structure

```
cambridge-practice/
├── python/                            # ✅ Created
│   ├── README.md                    # ✅ Course intro, setup guide (8.5KB)
│   ├── arcade-intro.html            # ✅ First sheet - live at:
│   │                                  #    https://jasperf.github.io/cambridge-practice/python/arcade-intro.html
│   ├── basics/                       # ✅ Empty, ready for:
│   │   ├── arcade-intro.html        # ✅ DONE - Arcade setup, first window
│   │   ├── sprites-graphics.html    # ✅ DONE - Working with images, sprites, SpriteLists
│   │   └── movement-physics.html     # ⬜ TODO - Position, velocity, keyboard
│   ├── platformer/                   # ✅ Empty, ready for:
│   │   ├── part1-project-setup.html      # ✅ DONE - Project structure, base class, constants
│   │   ├── part2-player.html            # ⬜ TODO - Player sprite, movement
│   │   ├── part3-platforms.html          # ⬜ TODO - Platform class, collision
│   │   ├── part4-jumping-gravity.html    # ⬜ TODO - Jump physics, gravity
│   │   ├── part5-camera-scrolling.html   # ⬜ TODO - Camera follows player
│   │   ├── part6-coins-collectibles.html # ⬜ TODO - Collect items, scoring
│   │   ├── part7-enemies.html            # ⬜ TODO - Enemy AI, collision
│   │   ├── part8-levels.html             # ⬜ TODO - Load 2 levels from files
│   │   ├── part9-polish.html             # ⬜ TODO - Graphics, sound, menu
│   │   └── CHALLENGE-extensions.html     # ⬜ TODO - Optional: power-ups, animations
│   └── challenges/                     # ✅ Empty, ready for:
│       ├── debugging-practice.html       # ⬜ TODO - Fix broken code snippets
│       ├── code-tracing.html             # ⬜ TODO - Trace execution, predict output
│       └── algorithm-quiz.html            # ⬜ TODO - Game logic puzzles
├── index.html                         # ✅ Updated with Python section & nav
├── AGENTS.md                          # ✅ Updated with commit constraints
└── docs/
    └── python-platformer-course.md      # ✅ This document (curriculum plan)
```

---

## 🎮 Game Specifications

### Core Features (All Required)
| Feature | Description | Sheet |
|---------|-------------|-------|
| Player | Sprite with left/right movement, jump | Part 2 |
| Platforms | Solid surfaces to stand on | Part 3 |
| Gravity | Realistic falling, jump arc | Part 4 |
| Collision | Player lands on platforms | Part 3 |
| Camera | Follows player, shows more world | Part 5 |
| Coins | Collectibles with score | Part 6 |
| Enemies | Basic AI (patrol), kill player | Part 7 |
| 2 Levels | Load from JSON/tiled files | Part 8 |
| Scoring | Points, lives, display | Part 6 |
| Graphics | Player/enemy sprites | Part 9 |
| Sound | Jump, coin, death effects | Part 9 |

### Optional Extensions (Challenge Sheet)
- Double jump / power-ups
- Enemy types (flying, stationary)
- Moving platforms
- Checkpoints
- Animations (running, jumping)
- Particle effects
- Game over / win screens
- High score persistence

---

## 📚 Part-by-Part Breakdown

### Phase 1: Arcade Fundamentals (Basics Folder)

#### Sheet: `arcade-intro.html` ✅ IMPLEMENTED
**Format:** Mixed in-browser + project setup
**Duration:** 30-45 min
**Status:** ✅ LIVE at https://jasperf.github.io/cambridge-practice/python/arcade-intro.html
**Topics:**
- Install Arcade on Mac: `pip install arcade`
- Create first window
- Game loop concept (`on_draw()`, `arcade.run()`)
- Drawing shapes (`arcade.draw_circle_filled`)
- Coordinate system (bottom-left origin, X right, Y up)

**In-Browser Exercises (7 questions, 10 marks total):**
1. **Q1 (1 mark)** - MCQ: "What command installs Arcade?" → `pip install arcade`
2. **Q2 (1 mark)** - MCQ: "What are the three parameters for arcade.Window()?" → width, height, title
3. **Q3 (1 mark)** - MCQ: "Where is the origin (0,0)?" → Bottom-left corner
4. **Q4 (2 marks)** - Code tracing: "What does `arcade.draw_circle_filled(100, 100, 50, RED)` draw?" with canvas visualization
5. **Q5 (2 marks)** - Debug: "Window opens but closes immediately" → Missing `arcade.run()`
6. **Q6 (1 mark)** - MCQ: "Which method draws everything each frame?" → `on_draw()`
7. **Q7 (2 marks)** - MCQ: "Position relative to center" → Right and above

**Interactive Elements:**
- SVG coordinate system diagram with click-to-test functionality
- Canvas visualization for Q4 code output
- Progress bar tracking completion
- Confetti celebration on ≥70% score

**Project Task:**
- **File:** Create `game.py`
- **Code:** Complete working example with window, background, text
- **Steps:** Create file, paste code, save, run with `python3 game.py`
- **Checkpoints:**
  1. ✓ Created `game.py` with code
  2. ✓ Game window opened successfully
  3. ✓ Saw "Hello, Arcade!" on dark blue background
- **Troubleshooting:** 4 common issues with solutions

---

#### Sheet: `sprites-graphics.html` ✅ IMPLEMENTED
**Format:** Mixed
**Duration:** 45 min
**Status:** ✅ LIVE at https://jasperf.github.io/cambridge-practice/python/sprites-graphics.html
**Topics:**
- Loading images
- Sprite class
- Scaling sprites
- Drawing sprites at positions

**In-Browser Exercises:**
1. MCQ: "What file format should sprite images be?" (PNG, JPG, etc.)
2. Code tracing: "Where does this sprite appear?" (click position on SVG grid)
3. Debug: Fix sprite not showing (missing `setup()` call)
4. Interactive: Drag sprite to correct position on SVG coordinate system

**Project Task:**
- Download provided player sprite image
- Load and display it at position (100, 100)
- Scale it to appropriate size
- Checkpoint: Sprite appears on screen

---

#### Sheet: `movement-physics.html`
**Format:** Mixed
**Duration:** 60 min
**Topics:**
- Keyboard input
- Position vs. change in position
- Velocity concept
- Frame-based movement

**In-Browser Exercises:**
1. MCQ: "Which method captures keyboard input?"
2. Code tracing: "Player starts at (0,0), moves right at 5 px/frame. Position after 10 frames?"
3. Debug: Fix movement code (velocity not being added to position)
4. Interactive: SVG with arrow keys, click to simulate movement, see position update

**Project Task:**
- Add keyboard controls to move player left/right
- Use velocity for smooth movement
- Add boundaries (can't go off-screen)
- Checkpoint: Player moves with arrow keys

---

### Phase 2: Platformer Core (Platformer Folder)

#### Sheet: `part1-project-setup.html` ✅ IMPLEMENTED
**Format:** Project guide with embedded checks
**Duration:** 30 min
**Status:** ✅ LIVE at https://jasperf.github.io/cambridge-practice/python/platformer/part1-project-setup.html
**Topics:**
- Project structure
- Game class inheritance
- Organizing code
- Constants for configuration

**Content:**
- Explanation of Arcade's `arcade.Window` and `arcade.View`
- Create proper project structure:
  ```
  mario-game/
  ├── main.py          # Entry point
  ├── game.py          # Game class
  ├── player.py        # Player class
  ├── assets/
  │   ├── sprites/
  │   └── sounds/
  └── levels/
      ├── level1.json
      └── level2.json
  ```
- Base Game class with window setup

**Checkpoints:**
1. Folder structure created ✓
2. `main.py` runs and shows empty window ✓
3. Game class instantiated correctly ✓

**Self-Assessment Questions (in-browser):**
1. "Why do we use a Game class?" (MCQ: organization, reusability, etc.)
2. "Where should sprite images be stored?" (MCQ)

---

#### Sheet: `part2-player.html`
**Format:** Project guide
**Duration:** 60 min
**Topics:**
- Player class extending `arcade.Sprite`
- Keyboard input handling
- Movement physics
- Sprite animation basics

**Project Tasks:**
1. Create `Player` class
2. Load player sprite
3. Implement `update()` method for movement
4. Add gravity simulation (preparation for Part 4)

**Code Snippet:**
```python
class Player(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__("assets/sprites/player.png", SCALE)
        self.center_x = x
        self.center_y = y
        
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
```

**Checkpoints:**
1. Player sprite appears on screen ✓
2. Pressing left/right moves player ✓
3. Player stops at screen edges ✓

**Self-Assessment:**
1. "What does `center_x` represent?" (MCQ)
2. "Why use `change_x` instead of directly setting `center_x`?" (MCQ)

---

#### Sheet: `part3-platforms.html`
**Format:** Project guide + interactive diagram
**Duration:** 90 min
**Topics:**
- Platform class
- Sprite lists
- Collision detection
- Standing on platforms

**Interactive Element (SVG):**
- Diagram showing player above platform
- Visualization of hit boxes
- Click to see collision detection in action

**Project Tasks:**
1. Create `Platform` class extending `arcade.Sprite`
2. Add multiple platforms at different heights
3. Implement collision: player can stand on platforms
4. Prevent falling through platforms

**Key Code:**
```python
# In Game class
def setup(self):
    self.platform_list = arcade.SpriteList()
    platform = Platform(100, 100)
    self.platform_list.append(platform)

def on_update(self, delta_time):
    # Check for collision with platforms
    hit_list = arcade.check_for_collision_with_list(
        self.player, self.platform_list
    )
    for platform in hit_list:
        # Handle collision (stop falling)
        if self.player.change_y < 0:
            self.player.change_y = 0
            self.player.center_y = platform.top
```

**Checkpoints:**
1. Platforms visible on screen ✓
2. Player can stand on platforms ✓
3. Player doesn't fall through platforms ✓

**Self-Assessment:**
1. "What does `check_for_collision_with_list` return?" (MCQ)
2. Debug exercise: Platform collision not working, find the bug

---

#### Sheet: `part4-jumping-gravity.html`
**Format:** Project guide + physics visualization
**Duration:** 90 min
**Topics:**
- Gravity simulation
- Jump mechanics
- Acceleration
- Terminal velocity (optional)

**Interactive Element (SVG):**
- Physics visualization: show jump arc trajectory
- Adjustable gravity slider (conceptual)
- Show velocity vectors

**Project Tasks:**
1. Add gravity constant
2. Apply gravity to player (constant downward acceleration)
3. Implement jump on key press
4. Prevent double-jumping (only jump when on ground)
5. Add jump sound effect

**Key Code:**
```python
# Constants
GRAVITY = 0.5
JUMP_VELOCITY = 12

# In Player class
is_on_ground = False

def update(self):
    # Apply gravity
    self.change_y -= GRAVITY
    
    # Move
    self.center_x += self.change_x
    self.center_y += self.change_y
    
    # Check if on ground
    self.is_on_ground = False

def jump(self):
    if self.is_on_ground:
        self.change_y = JUMP_VELOCITY
        arcade.play_sound(self.jump_sound)
```

**Checkpoints:**
1. Player falls when not on platform ✓
2. Pressing up/space makes player jump ✓
3. Jump height feels right ✓
4. Can't jump in mid-air ✓

**Self-Assessment:**
1. "Why subtract GRAVITY from change_y?" (MCQ: gravity pulls down, so negative)
2. "What happens if GRAVITY is 0?" (MCQ)
3. Code tracing: Calculate player's y position after 10 frames with jump

---

#### Sheet: `part5-camera-scrolling.html`
**Format:** Project guide
**Duration:** 60 min
**Topics:**
- Camera view
- Following player
- Viewport boundaries
- Smooth camera movement

**Project Tasks:**
1. Create camera that follows player
2. Set viewport margins (player can move partially off-screen)
3. Ensure camera doesn't show outside level boundaries
4. Smooth camera movement (optional)

**Key Code:**
```python
def setup(self):
    # Create camera
    self.camera = arcade.Camera(self.width, self.height)
    
    # Create sprite lists for each layer
    self.background_list = arcade.SpriteList()
    self.platform_list = arcade.SpriteList()
    self.player_list = arcade.SpriteList()
    
def on_draw(self):
    self.clear()
    
    # Activate camera
    self.camera.use()
    
    # Draw everything
    self.background_list.draw()
    self.platform_list.draw()
    self.player_list.draw()
    
def on_update(self, delta_time):
    # Position the camera
    self.camera.position = (
        self.player.center_x,
        self.player.center_y
    )
```

**Checkpoints:**
1. Camera follows player horizontally ✓
2. Camera follows player vertically ✓
3. Level boundaries respected ✓

---

#### Sheet: `part6-coins-collectibles.html`
**Format:** Project guide + scoring system
**Duration:** 75 min
**Topics:**
- Collectible items
- Collision detection for collection
- Score tracking
- Removing collected items
- Sound effects

**Project Tasks:**
1. Create `Coin` class
2. Add coins to level
3. Detect player-coin collision
4. Remove coin when collected
5. Increment score
6. Play collection sound
7. Display score on screen

**Key Code:**
```python
class Coin(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__("assets/sprites/coin.png", COIN_SCALE)
        self.center_x = x
        self.center_y = y

# In Game class
def setup(self):
    self.coin_list = arcade.SpriteList()
    # Add coins...
    
def on_update(self, delta_time):
    # Check for coin collection
    coins = arcade.check_for_collision_with_list(
        self.player, self.coin_list
    )
    for coin in coins:
        coin.remove_from_sprite_lists()
        self.score += 1
        arcade.play_sound(self.coin_sound)
```

**Checkpoints:**
1. Coins appear on platforms ✓
2. Collecting coin increases score ✓
3. Coin disappears when collected ✓
4. Sound plays on collection ✓

**Self-Assessment:**
1. "Why `remove_from_sprite_lists()` instead of just deleting?" (MCQ)
2. Debug: Coins can be collected multiple times, find the bug

---

#### Sheet: `part7-enemies.html`
**Format:** Project guide + AI visualization
**Duration:** 90 min
**Topics:**
- Enemy class
- Simple AI (patrol between two points)
- Player-enemy collision
- Lives system
- Game over state

**Interactive Element (SVG):**
- Show enemy patrol path
- Visualize detection range
- Animate patrol movement

**Project Tasks:**
1. Create `Enemy` class
2. Implement patrol behavior (move between point A and B)
3. Detect player-enemy collision
4. Decrement lives when hit
5. Game over when lives reach 0
6. Reset level or go to game over screen

**Key Code:**
```python
class Enemy(arcade.Sprite):
    def __init__(self, x, y, left_boundary, right_boundary):
        super().__init__("assets/sprites/enemy.png", ENEMY_SCALE)
        self.center_x = x
        self.center_y = y
        self.left_boundary = left_boundary
        self.right_boundary = right_boundary
        self.change_x = -1  # Start moving left
        
    def update(self):
        self.center_x += self.change_x
        
        # Patrol logic
        if self.center_x < self.left_boundary:
            self.change_x = 1  # Move right
        elif self.center_x > self.right_boundary:
            self.change_x = -1  # Move left

# In Game class
def on_update(self, delta_time):
    # Check for enemy collision
    enemies = arcade.check_for_collision_with_list(
        self.player, self.enemy_list
    )
    if enemies:
        self.lives -= 1
        if self.lives <= 0:
            # Game over
            self.game_over = True
```

**Checkpoints:**
1. Enemies patrol back and forth ✓
2. Touching enemy reduces lives ✓
3. Game over when lives = 0 ✓

**Self-Assessment:**
1. "How would you make enemies move faster?" (MCQ)
2. "What happens if player jumps on enemy?" (Currently: same as touching. Optional: add stomp mechanic)

---

#### Sheet: `part8-levels.html`
**Format:** Project guide + level design
**Duration:** 90 min
**Topics:**
- Level design
- Loading levels from files
- JSON format for level data
- Level switching
- Starting positions

**Project Tasks:**
1. Design level format (JSON structure)
2. Create level1.json and level2.json
3. Load level data
4. Parse JSON and create platforms, coins, enemies
5. Add level completion (reach flag/door)
6. Switch to next level

**Level JSON Format:**
```json
{
  "name": "Level 1",
  "player_start": {"x": 50, "y": 100},
  "platforms": [
    {"x": 100, "y": 50, "width": 200, "height": 20},
    {"x": 400, "y": 100, "width": 150, "height": 20}
  ],
  "coins": [
    {"x": 200, "y": 70},
    {"x": 450, "y": 120}
  ],
  "enemies": [
    {"x": 300, "y": 50, "left": 250, "right": 350}
  ],
  "exit": {"x": 500, "y": 100, "width": 30, "height": 50}
}
```

**Key Code:**
```python
import json

def load_level(self, level_num):
    with open(f"levels/level{level_num}.json") as f:
        level_data = json.load(f)
    
    # Clear existing sprites
    self.platform_list = arcade.SpriteList()
    self.coin_list = arcade.SpriteList()
    self.enemy_list = arcade.SpriteList()
    
    # Create platforms
    for p in level_data["platforms"]:
        platform = Platform(p["x"], p["y"], p["width"], p["height"])
        self.platform_list.append(platform)
    
    # Create coins, enemies, etc.
    # ...
    
    # Position player
    self.player.center_x = level_data["player_start"]["x"]
    self.player.center_y = level_data["player_start"]["y"]
```

**Checkpoints:**
1. Level loads from JSON file ✓
2. All platforms, coins, enemies in correct positions ✓
3. Level 1 completes, advances to level 2 ✓

---

#### Sheet: `part9-polish.html`
**Format:** Project guide + creative freedom
**Duration:** 120 min
**Topics:**
- Graphics improvement
- Sound effects
- Background music
- Start menu
- Game over screen
- Win screen

**Project Tasks:**
1. Add background images
2. Add animations (player running, jumping)
3. Add all sound effects (jump, coin, death, game over)
4. Create start menu with instructions
5. Create game over screen with restart option
6. Create level complete screen
7. Add high score tracking (optional)

**Key Code:**
```python
# In Game class
def on_draw(self):
    if self.state == "MENU":
        self.draw_menu()
    elif self.state == "GAME":
        self.draw_game()
    elif self.state == "GAME_OVER":
        self.draw_game_over()
    
def draw_menu(self):
    self.clear()
    arcade.draw_text("Mario-Style Platformer", 
                    self.width/2, self.height/2 + 100,
                    arcade.color.WHITE, font_size=50, anchor_x="center")
    arcade.draw_text("Press SPACE to Start",
                    self.width/2, self.height/2 - 50,
                    arcade.color.YELLOW, font_size=24, anchor_x="center")
```

**Checkpoints:**
1. Start menu appears first ✓
2. All sound effects working ✓
3. Game over screen shows score ✓
4. Can restart game ✓

---

### Phase 3: Challenges & Extensions

#### Sheet: `CHALLENGE-extensions.html`
**Format:** Self-directed challenges with hints
**Duration:** Variable

**Challenge Ideas:**

1. **Double Jump** — Press jump twice for higher jump
   - Track if player has jumped
   - Allow second jump with different velocity

2. **Power-ups** — Temporary invincibility, speed boost
   - New sprite type
   - Timer for power-up duration
   - Visual indicator

3. **Moving Platforms** — Platforms that move horizontally/vertically
   - Add velocity to Platform class
   - Add boundary checking

4. **Flying Enemies** — Enemies that move in patterns
   - Different movement AI
   - Maybe follow player

5. **Checkpoints** — Save progress in level
   - Remember last checkpoint position
   - Respawn there on death

6. **Animations** — Smooth sprite animations
   - Use sprite sheets
   - Track animation frames

7. **Particle Effects** — Visual feedback
   - Jump dust
   - Coin collection sparkles
   - Explosion on death

8. **High Score System** — Persistent scores
   - Save to file
   - Display high score table

**Format for Each Challenge:**
- Description of feature
- Hints (revealed progressively)
- Starter code snippets
- Checklist of requirements
- Self-assessment: "Did you implement X correctly?"

---

## 🎨 Asset Requirements

We need to provide or guide creation of these assets:

### Sprites (PNG, transparent background)
| Asset | Size | Notes |
|-------|------|-------|
| Player (idle) | 32x48 | Standing still |
| Player (run) | 32x48 | 4-6 frames animation |
| Player (jump) | 32x48 | Mid-air pose |
| Platform | 32x32 | Tileable, multiple types |
| Coin | 16x16 | Gold, spinning animation |
| Enemy (type 1) | 32x32 | Basic goomba-style |
| Exit/Flag | 32x64 | For level completion |
| Background | 800x600+ | Parallax layers optional |

### Sounds (WAV or OGG)
- jump.wav
- coin.wav
- death.wav
- game_over.wav
- level_complete.wav
- background_music.wav (optional)

### Strategy for Assets:
1. **Provide simple pixel art sprites** — Create basic 16x16 or 32x32 sprites as base64 encoded images in the HTML worksheets, or provide download links
2. **Student can create their own** — Encourage customization
3. **Use emoji placeholders** — For quick testing: use emoji characters as temporary sprites
4. **Free resources** — Point to Kenney.nl game assets (free, CC0 license)

---

## 🎯 Assessment & Progress Tracking

### In Each Sheet:
- **Auto-checked questions** — MCQ, code tracing, debugging (instant feedback)
- **Self-assessment checklists** — "I have completed X" checkboxes
- **Project checkpoints** — "Run your code and verify Y happens"
- **Hint system** — Progressive hints before showing answer
- **Score tracking** — Percentage complete per sheet

### Overall Course Tracking:
- Each sheet has its own score
- Progress saved to localStorage
- Final certificate/achievement at end

---

## ⏱ Estimated Timeline

| Phase | Sheets | Time | Total |
|-------|--------|------|-------|
| Arcade Fundamentals | 3 | 2.5 hrs | 2.5 hrs |
| Platformer Core | 5 | 7.5 hrs | 10 hrs |
| Polish & Levels | 2 | 3.5 hrs | 13.5 hrs |
| Challenges | 1+ | 2-5 hrs | 15.5-18.5 hrs |

**Total:** ~15-20 hours for complete game

Can be done at student's pace, one sheet per session.

---

## 🔧 Technical Requirements

### For In-Browser Worksheets:
- Modern browser (Chrome, Safari, Firefox)
- No internet required after loading
- Works on iPad/tablet (bonus)

### For Coding on Mac:
- Python 3.8+ installed
- Arcade library: `pip install arcade`
- Text editor (VS Code, PyCharm, or any)
- Terminal for running: `python main.py`

---

## ✅ Implementation Status

### Completed ✅

#### 1. Foundation Setup
- ✅ **docs/python-platformer-course.md** — This curriculum plan document
- ✅ **python/ folder structure** — Created with `basics/`, `platformer/`, `challenges/` subfolders
- ✅ **python/README.md** — Comprehensive course documentation (8.5KB)
  - Getting started guide
  - Python installation
  - Arcade installation
  - Course structure overview
  - Troubleshooting tips
  - Asset resources
  - Learning path

#### 2. First Worksheet: arcade-intro.html
- ✅ **Full interactive sheet** (55KB) with:
  - Hero section with course intro, duration, difficulty
  - Concepts section:
    - What is Arcade (with comparison to Pygame)
    - Installation instructions (`pip3 install arcade`)
    - The Game Loop explanation
    - Coordinate System with interactive SVG diagram (click to see coordinates)
  - Exercises section with **7 questions** (10 marks total):
    - Q1: Install command MCQ
    - Q2: Window parameters MCQ
    - Q3: Coordinate origin MCQ
    - Q4: Code tracing (draw_circle_filled) with canvas visualization
    - Q5: Debugging challenge (missing arcade.run())
    - Q6: Drawing method MCQ (on_draw)
    - Q7: Coordinate position MCQ
  - Project Task section:
    - Complete code for first game window
    - Step-by-step instructions
    - Self-verification checkpoints (3 items)
    - Troubleshooting guide
  - Full state management:
    - Score tracking with localStorage
    - Progress bar
    - Confetti celebration (≥70%)
    - Results panel with grade, score, time
- ✅ **Code block fix** — Fixed CSS counter issue causing squished characters
  - Changed from `.code-line.numbers span` to `.code-line::before`
  - Added better monospace font stack: SF Mono, Monaco, Inconsolata, Fira Code, Fira Mono, DM Mono
  - Proper line numbering with CSS counters
- ✅ **index.html updated** — Added Python section with:
  - Navigation link
  - Hero tag
  - Grid section with live arcade-intro card
  - Placeholder cards for upcoming sheets

#### 3. Platformer Part 1: Project Setup
- ✅ **python/platformer/part1-project-setup.html** — First platformer sheet (Full interactive sheet)
  - Concepts: Project organization, Arcade's View system, folder structure
  - Exercises: 7 questions (10 marks total) covering project structure, Game class, constants
  - Project Task: Create mario-game/ folder structure with main.py, game.py, assets/, levels/
  - Starter Code: Complete main.py entry point and Game class skeleton
  - LIVE at https://jasperf.github.io/cambridge-practice/python/platformer/part1-project-setup.html

#### 4. Basics: Sprites & Graphics
- ✅ **python/sprites-graphics.html** — Second basics sheet (Full interactive sheet)
  - Concepts: Sprites, Sprite class, loading images, scaling, SpriteLists
  - Exercises: 6 questions (10 marks total) covering file formats, scale, positioning, debugging
  - Project Task: Add player sprite to existing game project with SpriteList
  - Interactive: Coordinate grid visualization
  - LIVE at https://jasperf.github.io/cambridge-practice/python/sprites-graphics.html

#### 5. Basics: Movement & Physics
- ✅ **python/basics/movement-physics.html** — Third basics sheet (Full interactive sheet)
  - Concepts: Keyboard input, position vs velocity, frame-based movement
  - Exercises: 6 questions covering keyboard methods, code tracing, debugging
  - Project Task: Add keyboard controls to move player left/right with velocity
  - Interactive: SVG with clickable arrow keys to simulate movement

#### 6. Platformer Part 1: Project Setup
- ✅ **python/platformer/part1-project-setup.html** — First platformer sheet (Full interactive sheet)
  - Concepts: Project organization, Arcade's View system, folder structure
  - Exercises: 7 questions (10 marks total) covering project structure, Game class, constants
  - Project Task: Create mario-game/ folder structure with main.py, game.py, assets/, levels/
  - Starter Code: Complete main.py entry point and Game class skeleton
  - LIVE at https://jasperf.github.io/cambridge-practice/python/platformer/part1-project-setup.html

#### 7. Platformer Part 2: Player
- ✅ **python/platformer/part2-player.html** — Player movement sheet (Full interactive sheet)
  - Concepts: Player class extending arcade.Sprite, keyboard input handling, movement physics
  - Exercises: 7 questions (10 marks total) covering inheritance, super(), movement speed constants
  - Project Task: Create Player class with movement controls and boundaries
  - LIVE at https://jasperf.github.io/cambridge-practice/python/platformer/part2-player.html

#### 8. Platformer Part 3: Platforms
- ✅ **python/platformer/part3-platforms.html** — Platform collision sheet (Full interactive sheet)
  - Concepts: Platform class, SpriteLists, collision detection, landing on platforms
  - Exercises: 7 questions (10 marks total) covering SpriteLists, collision functions, platform positioning
  - Project Task: Create Platform class, add multiple platforms, implement collision detection
  - Interactive: Canvas-based collision visualization
  - LIVE at https://jasperf.github.io/cambridge-practice/python/platformer/part3-platforms.html

#### 9. Platformer Part 4: Jumping & Gravity
- ✅ **python/platformer/part4-jumping-gravity.html** — Physics implementation sheet (Full interactive sheet)
  - Concepts: Gravity simulation, jump mechanics, acceleration, ground detection
  - Exercises: 7 questions (10 marks total) covering gravity effects, jump timing, debugging
  - Project Task: Add GRAVITY constant, JUMP_VELOCITY, ground tracking, jump method, collision handling
  - Interactive: Jump arc visualization with adjustable gravity and jump velocity sliders
  - Canvas animation shows trajectory path and velocity over time

#### 10. Git & Deployment
- ✅ All files committed with clean messages (no AI co-authorship)
- ✅ Pushed to GitHub main branch
- ✅ Auto-deployed to GitHub Pages:
  - https://jasperf.github.io/cambridge-practice/python/arcade-intro.html
  - https://jasperf.github.io/cambridge-practice/python/sprites-graphics.html
  - https://jasperf.github.io/cambridge-practice/python/platformer/part1-project-setup.html
- ✅ AGENTS.md updated with commit message constraints

### In Progress 🚧

- ⏳ Awaiting feedback on first sheet before continuing

### Remaining 📋

- ⬜ Create part5-camera-scrolling.html through part9-polish.html
- ⬜ Create challenge sheets (debugging-practice.html, code-tracing.html, algorithm-quiz.html)
- ⬜ Create simple sprite assets
- ⬜ Test complete course end-to-end

---

## 📝 Next Steps (Implementation Order)

1. **Create docs folder content** (THIS FILE) ✅
2. **Set up python/ folder structure** ✅
3. **Create arcade-intro.html** — First sheet, test the format ✅
4. **Fix code block rendering** — CSS counters for line numbers ✅
5. **Add Python section to index.html** ✅
6. **Update AGENTS.md** with commit constraints ✅
7. **Create part1-project-setup.html** — First platformer sheet ✅
8. **Create sprites-graphics.html** — Second basics sheet ✅
9. **Create movement-physics.html** — Third basics sheet ✅
10. **Create part2-player.html** — Player movement ✅
11. **Create part3-platforms.html** — Platform collision ✅
12. **Create part4-jumping-gravity.html** — Gravity & Jumping ✅
13. **Create part5-camera-scrolling.html** — Camera follows player
14. **Iterate and refine** based on student feedback
15. **Create remaining sheets** one by one (part6-part9)
16. **Create challenge sheets**
17. **Create assets** (simple sprites, sounds)
18. **Test complete course** end-to-end

---

## 🎓 Learning Outcomes

By the end of this course, student will:

1. **Python Skills:**
   - Object-oriented programming (classes, inheritance)
   - Lists and dictionaries for game state
   - File I/O (loading levels)
   - Event-driven programming (keyboard input)
   - Math for game physics (velocity, acceleration, collision)

2. **Game Development Skills:**
   - Game loop architecture
   - Sprite management
   - Collision detection
   - Game state management
   - Level design
   - Asset management

3. **Problem Solving:**
   - Debugging code
   - Breaking problems into smaller pieces
   - Testing and iteration
   - Reading documentation

4. **Soft Skills:**
   - Following step-by-step instructions
   - Attention to detail
   - Persistence through challenges
   - Creativity in customization

---

## 📊 Comparison: Arcade vs Pygame

| Feature | Arcade | Pygame | Decision |
|---------|--------|--------|----------|
| Ease of Use | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | **Arcade** |
| Modern API | ✅ Yes | ❌ Older | **Arcade** |
| Camera Support | ✅ Built-in | ⚠️ Manual | **Arcade** |
| Physics Engine | ✅ Simple | ⚠️ Manual | **Arcade** |
| Documentation | ✅ Excellent | ✅ Good | Tie |
| Community | ⚠️ Smaller | ✅ Large | Pygame |
| Installation | ✅ Easy | ✅ Easy | Tie |
| Performance | ✅ Good | ✅ Good | Tie |

**Winner: Arcade** — Better for beginners, built-in features we need, cleaner API.

---

## 🎉 Celebration & Motivation

- Each completed sheet: Confetti animation (like existing sheets)
- Each milestone (Part 2, 4, 6, 8): Special badge/achievement
- Completed game: Certificate of completion
- Optional: Share game with friends/family
- Optional: Publish on itch.io (free game hosting)

---

## 📞 Support & Troubleshooting

Common issues and solutions to include in sheets:

1. **"ModuleNotFoundError: No module named 'arcade'"**
   - Solution: `pip install arcade` (or `pip3 install arcade`)

2. **"Image not found" errors**
   - Solution: Check file paths, ensure images in correct folder

3. **Window closes immediately**
   - Solution: Add `arcade.run()` at end of main.py

4. **Player doesn't move**
   - Solution: Check keyboard bindings, ensure `on_key_press` registered

5. **Player falls through platforms**
   - Solution: Check collision detection code, ensure using `check_for_collision_with_list`

---

## 🔄 Iteration Plan

1. **V1: Minimal Viable** — arcade-intro, part1, part2 (player movement)
2. **V2: Core Gameplay** — Add parts 3-5 (platforms, jumping, camera)
3. **V3: Complete Game** — Add parts 6-8 (coins, enemies, levels)
4. **V4: Polish** — Add part9 and challenges
5. **Continuous** — Fix bugs, improve explanations based on student feedback

---

## ✅ Ready to Implement?

Once this plan is approved, I can start creating the actual HTML worksheets following the existing repo conventions:

- Match the dark theme CSS from circuits.html
- Use the standard topbar: "Student's Study Hub" logo, back-link, timer, score pill (see AGENTS.md "Sheet Header Pattern")
- Use the same state management pattern (state object, marks, etc.)
- Include the same interactive elements (confetti with `id="confetti-canvas"`, progress bar, score pills)
- Follow the same card-based layout for questions
- Add the Python section to index.html

**First sheet to create:** `python/arcade-intro.html` — This will establish the pattern for all subsequent sheets.

Would you like me to proceed with implementation?
