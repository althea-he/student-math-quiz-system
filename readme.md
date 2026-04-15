# 🎯 Student Math Quiz System | 学生算术测试系统

## 📌 Overview
This project is a Python-based student math quiz system designed to generate arithmetic problems, manage student records, and evaluate performance.

该项目实现了一个基于 Python 的学生算术测试系统，支持自动出题、学生成绩记录与查询，以及基本的数据管理功能。

---

## 🚀 Key Features

- 🧮 **Random Problem Generation**
  - Generates arithmetic questions (+, −, ×, ÷)
  - Ensures valid operations (e.g., no division by zero, integer division)

- 🆔 **Unique Student ID System**
  - Automatically assigns unique IDs to students
  - Prevents duplication using pre-generated ID pool

- 📊 **Record Management**
  - Stores student results in file (`record.txt`)
  - Supports result retrieval and ranking

- ⚠️ **Robust Input Handling**
  - Handles invalid input gracefully
  - Includes edge-case validation and error prompts

---

## 🧠 System Design

### Core Modules
- `create_id()`: Generates and assigns unique student IDs
- `calc()`: Generates arithmetic problems with constraints
- Record storage: Maintains persistent results using file I/O

### Design Highlights
- Separation between problem generation and record management
- Input validation ensures system stability
- Lightweight and file-based storage (no external database)

---

## 📂 Repository Structure
```
├── main_program_算术测试系统.py        # Main program
├── project_specification_项目要求.pdf   # Project requirements
├── system_design_doc_程序设计文档.docx  # System design documentation
├── test_report_测试报告.docx           # Testing report
├── user_manual_用户帮助手册.docx        # User manual
├── screenshots_demo_展示截图/           # Code demonstration screenshots
├── screenshots_runtime_运行截图/        # Runtime & output screenshots
└── README.md
```

---

## 🛠️ Tech Stack

- Python
- File I/O
- Basic data structures (lists, dictionaries)

---

## 📸 Demo

### Code Demonstration
See: `screenshots_demo_展示截图/`

### Runtime Examples
See: `screenshots_runtime_运行截图/`

Includes:
- Normal execution flows
- Record output
- Error handling (invalid input, missing records)

---

## 📈 Key Takeaways

- Demonstrates end-to-end system design in Python
- Implements basic data persistence without databases
- Emphasizes robustness through input validation
- Shows structured programming and modular design

---

## ✨ Notes

This project was originally developed as a course assignment, and later refined for clarity, structure, and reproducibility.

该项目最初为课程作业，现已整理优化用于展示系统设计与编程能力。
