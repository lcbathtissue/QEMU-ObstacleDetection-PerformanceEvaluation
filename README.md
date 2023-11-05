# Performance Evaluation of Object Detection in Embedded Systems

## Introduction

In embedded systems precision and efficiency are important and the choice of hardware architecture is a large factor in the outcomes of critical applications, especially in object detection. This repository hosts an analysis of object detection performance, employing the YOLO (You Only Look Once) framework across three distinct architectures: AMD64 (Host), i386 (VM #1), and x86_64 (VM #2) within QEMU.

## Report

For detailed insights into the performance evaluation and analysis, please refer to the full report provided in the [Report_Embedded_Assignment_2.pdf](Report_Embedded_Assignment_2.pdf) file located in the root of this project repository.

## Dataset

The project dataset is available in a compressed form. Some files were too large for GitHub, so we have provided a download link to the complete project dataset, which includes all the necessary input videos and processed data files. You can download the full project from my website by clicking [here](http://aldenocain.com/QEMU-ObstacleDetection-PerformanceEvaluation/full-project.zip).

## Code and Resources

- **'darknet-driver':** A directory containing the code for automating object detection on images.
- **'darknet-csv-parser':** A directory containing the code for parsing output files and storing data in CSV format.
- **'file-server':** A directory hosting the Flask server code for facilitating file transfer from QEMU machines to the host.
- **'video-cropper' and 'video-frame-grabber':** Directories with scripts for video cropping and frame extraction.
- **'data.xlsx':** An Excel file consolidating the dataset for in-depth analysis.
- **'file-server.py':** The Python script for running the Flask server.

## Performance Comparison

Analysis revealed variations in object detection performance among the three systems assessed. The host machine, equipped with the AMD64 architecture, exhibited the highest performance in real-time object detection, followed by the x86_64 Ubuntu Server QEMU emulated system and the i386 Raspbian OS-based VM presented notably slower performance, primarily due to its more constrained resource allocation, especially in terms of RAM.
