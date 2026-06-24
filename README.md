{\rtf1\ansi\ansicpg1252\cocoartf2870
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Code-A-Difference: Unified Classroom App\
\
An assistive technology tool designed to help students interact with classroom software using simple, AI-powered hand gestures.\
\
## How It Works\
The app uses a Mac's webcam to track user movements in real-time:\
* **Face Tracking:** Automatically establishes a "Trigger Line" right at nose level.\
* **Hand Tracking:** Tracks the student's wrist position.\
* **The Action:** When the student raises their hand so their wrist goes above their nose line, the app simulates a **Spacebar** keypress to trigger switch-accessible software or classroom games.\
\
## Repository Contents\
* `Unified_Classroom_App.py`: The core Python script utilizing OpenCV and MediaPipe.\
* `Unified_Classroom_App.spec`: The configuration blueprint used to bundle the script into a standalone Mac application.}