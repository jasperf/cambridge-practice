# Python Platformer Game Course

> **Build a Mario-style platformer game with Python and Arcade!**

---

## 🎮 About This Course

This interactive course teaches you **game development with Python** using the [Arcade library](https://api.arcade.academy/). Through a combination of in-browser worksheets and hands-on coding projects, you'll build a complete 2-level platformer game from scratch.

### 🎯 What You'll Build

By the end of this course, you'll have a fully functional platformer game featuring:

- **Player character** with smooth movement and jumping
- **Platforms** to stand on and jump between
- **Gravity physics** for realistic movement
- **Camera scrolling** to explore large levels
- **Coins** to collect with score tracking
- **Enemies** with AI patrol behavior
- **Two complete levels** loaded from JSON files
- **Polish** - graphics, sound effects, menus, and more!

### 🐍 Prerequisites

Before starting, you should be comfortable with:

- Python basics (variables, loops, conditionals)
- Functions and parameters
- Lists and dictionaries
- Basic object-oriented programming (classes)

If you're new to Python, complete a beginner Python course first.

---

## 🚀 Getting Started

### 1. Install Python

Make sure you have **Python 3.8 or newer** installed on your Mac.

Check your Python version:
```bash
python3 --version
```

If you don't have Python, download it from [python.org](https://www.python.org/downloads/)

### 2. Install Arcade

Open **Terminal** and run:

```bash
pip3 install arcade
```

Verify the installation worked:
```bash
python3 -c "import arcade; print('Arcade is ready!')"
```

You should see: `Arcade is ready!`

### 3. Start the Course

Begin with the first worksheet:
- **[Arcade Introduction](arcade-intro.html)** - Learn about Arcade, install it, and create your first window

---

## 📁 Course Structure

```
python/
├── README.md                    # This file - course overview
├── arcade-intro.html            # ✅ Start here!
├── sprites-graphics.html         # Working with images and sprites
└── movement-physics.html         # Keyboard input and movement

python/platformer/
├── part1-project-setup.html      # Project structure and base class
├── part2-player.html            # Player sprite and movement
├── part3-platforms.html          # Platforms and collision
├── part4-jumping-gravity.html    # Jump physics and gravity
├── part5-camera-scrolling.html   # Camera that follows player
├── part6-coins-collectibles.html # Collect items and score
├── part7-enemies.html            # Enemy AI and danger
├── part8-levels.html             # Load levels from files
└── part9-polish.html             # Graphics, sound, menus

python/challenges/
├── debugging-practice.html       # Fix broken code
├── code-tracing.html             # Trace execution
└── algorithm-quiz.html            # Game logic puzzles
```

---

## 🎓 Learning Path

### Phase 1: Arcade Fundamentals (2.5 hours)
1. **[Arcade Introduction](arcade-intro.html)** - Setup, first window, game loop, drawing (30-45 min)
2. **Sprites & Graphics** - Loading images, working with sprites (45 min)
3. **Movement & Physics** - Keyboard input, velocity, boundaries (60 min)

### Phase 2: Platformer Core (7.5 hours)
4. **Part 1: Project Setup** - File structure, game class (30 min)
5. **Part 2: Player** - Player sprite, movement controls (60 min)
6. **Part 3: Platforms** - Solid surfaces, collision detection (90 min)
7. **Part 4: Jumping & Gravity** - Physics, jump mechanics (90 min)
8. **Part 5: Camera** - Scrolling view (60 min)

### Phase 3: Game Features (3.5 hours)
9. **Part 6: Coins** - Collectibles, scoring (75 min)
10. **Part 7: Enemies** - AI patrol, lives system (90 min)
11. **Part 8: Levels** - Load from JSON, level switching (90 min)

### Phase 4: Polish & Extensions (2-5 hours)
12. **Part 9: Polish** - Menus, sound, graphics (120 min)
13. **Challenge Sheet** - Optional extensions (variable)

---

## 📚 How the Worksheets Work

Each worksheet is a **self-contained HTML file** that works in your browser:

- **✅ Auto-checked questions** - Multiple choice, code tracing, debugging with instant feedback
- **💡 Hint system** - Get help when you're stuck
- **📝 Project tasks** - Hands-on coding on your Mac
- **🎯 Checkpoints** - Verify your code works correctly
- **🎉 Progress tracking** - Scores saved to your browser
- **🎊 Celebration** - Confetti when you complete a sheet!

### Using the Worksheets

1. **Open in browser**: Double-click any `.html` file to open it
2. **Answer questions**: Click to select answers, then "Check Answer"
3. **Get hints**: Use the "Hint" button if you're stuck
4. **Do project tasks**: Code on your Mac following the instructions
5. **Track progress**: Your scores are saved automatically

---

## 🐛 Troubleshooting

### Common Problems & Solutions

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError: No module named 'arcade'` | Run `pip3 install arcade` |
| Window opens but closes immediately | You forgot `arcade.run()` at the end of your file |
| Player doesn't move | Check your `on_key_press` method registration |
| Player falls through platforms | Ensure you're using `arcade.check_for_collision_with_list()` |
| Images not showing | Check file paths are correct, images are in the right folder |

### Still Stuck?

- Check the **code examples** in each worksheet carefully
- Look at the **troubleshooting section** at the bottom of each sheet
- Review the **previous sheets** - you might have missed a key concept
- Try **restarting your code** from the provided template

---

## 🎨 Assets

You'll need some basic game assets (sprites and sounds). Options:

### Option 1: Create Your Own (Recommended)
Draw simple pixel art sprites using:
- [Piskel](https://www.piskelapp.com/) - Free online pixel art editor
- [Aseprite](https://www.aseprite.org/) - Paid but excellent ($20)

### Option 2: Use Free Assets
Download free game assets from:
- [Kenney.nl](https://kenney.nl/) - CC0 licensed (free for any use)
- [OpenGameArt.org](https://opengameart.org/) - Various licenses
- [itch.io/free](https://itch.io/game-assets/free) - Free game assets

### Option 3: Use Emoji Placeholders
For quick testing, you can use emoji as temporary sprites:
```python
# In your code, use text instead of sprites
arcade.draw_text("🟥", x, y, arcade.csscolor.WHITE, 24)
```

---

## 🏆 Achievement Badges

Complete each milestone to earn a badge:

- **🟢 Arcade Apprentice** - Complete Arcade Introduction sheet
- **🟡 Sprite Master** - Complete all Basics sheets
- **🟠 Platformer Pro** - Complete Part 2 (Player movement)
- **🔴 Collision Champion** - Complete Part 3 (Platforms)
- **🟣 Physics Expert** - Complete Part 4 (Gravity & Jumping)
- **🟤 Game Developer** - Complete all sheets!

---

## 📖 Additional Resources

### Arcade Documentation
- [Official Arcade API Documentation](https://api.arcade.academy/)
- [Arcade Examples on GitHub](https://github.com/pythonarcade/arcade/tree/development/examples)

### Python Resources
- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [W3Schools Python](https://www.w3schools.com/python/)
- [Real Python](https://realpython.com/)

### Game Development Concepts
- [Game Loop Explained](https://gafferongames.com/post/what_every_programmer_needs_to_know_about_game_loops/)
- [2D Collision Detection](https://developer.mozilla.org/en-US/docs/Games/Tutorials/2D_Breakout_game_pure_JS/Collision_detection)

---

## 💬 Feedback & Questions

Have questions or found a bug?

- **For code issues**: Double-check your work against the examples in the worksheets
- **For concept questions**: Review the info boxes and try the exercises again
- **For bugs in the worksheets**: Check the GitHub repository

---

## 🎉 Completing the Course

Once you've finished all sheets:

1. **Test your game** thoroughly
2. **Customize it** - add your own levels, graphics, features
3. **Share it** with friends and family
4. **Publish it** (optional) on [itch.io](https://itch.io/) - it's free!

### What's Next?

After this course, try:
- Adding **power-ups** (double jump, invincibility)
- Creating **more levels** with increasing difficulty
- Adding **sound effects and music**
- Implementing a **high score system**
- Building a **different type of game** (puzzle, RPG, shooter)

---

**Happy Coding! 🐍🎮**

*Last updated: June 2026*
