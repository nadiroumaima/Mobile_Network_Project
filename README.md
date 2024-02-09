# Communication Networks Performance Evaluation

## Introduction
In the realm of communication networks, the effectiveness of congestion control protocols, notably TCP, plays a pivotal role in ensuring optimal and dependable data transfer. This study employs NS2 (Network Simulator 2), a widely acknowledged simulation tool, to model and assess the performance of two TCP variants: TCP New Reno and TCP Vegas.

## Requirements
- **NS2 (Network Simulator 2):** Version 2.35 is required to execute the NS script.
  - Download NS2: [https://www.nsnam.com/2020/06/installation-of-ns2-ns-235-in-ubuntu.html]

## Execution
To run the simulation, follow these steps:

1. Run the NS script using ns2.35:
`ns nsanet.tcl`

2. Generate the trace file using Nam:
`nam sanet.nam`

3. Use AWK script to filter the trace file and redirect the output:
`awk -f script_output.awk sanet.tr > output.txt`


4. Visualize the output using plots.py.

## Visualization
To visualize the results, utilize the provided plot.py script. Customize and execute it based on your preferences and requirements.

## Note
Ensure that all the required dependencies, including NS2 version 2.35, are properly installed before running the simulation and visualization scripts.

For any issues or inquiries, please refer to the documentation or contact the relevant support channels for NS2.
