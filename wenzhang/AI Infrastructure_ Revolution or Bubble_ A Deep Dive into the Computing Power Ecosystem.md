# AI Infrastructure: Revolution or Bubble? A Deep Dive into the Computing Power Ecosystem

# Is AI Infrastructure a Bubble or a Revolution? A Deep Dive into AI Computing Power Ecosystem

In this article, we'll explore the AI infrastructure landscape, dissecting the roles, competitive dynamics, and commercial logics of chips, PCBs, optical modules, switches, cooling systems, and power systems in AI computing power infrastructure\.

## Is AI Infrastructure a Bubble?

The Star Gate Project in the US, initiated by OpenAI, SoftBank, and Oracle, is a prime example\. With a planned investment of $500 billion (equivalent to Thailand's annual GDP), it's just the tip of the iceberg. In 2025, the combined capital expenditure of North America's top five tech giants reached approximately $403\.6 billion, and it's expected to rise to $690 billion in 2026\.

These figures translate to real revenues for upstream companies\. For instance, **Nvidia**, the "shovel seller" in this gold rush, saw its revenue surge from 186 billion yuan in early 2023 to 1\.49 trillion yuan in early 2026\. AI server OEM **VIAI** quadrupled its revenue in just two to three years\. Companies across the supply chain, from switches and optical modules to storage chips and PCBs, have all reported significant growth\.

The driving force behind this growth lies in the extreme hunger for computing power from downstream large models\. AI large models, with their trillion\-level parameters, require massive computing resources for both training and inference\. Training a large model might need 100,000 GPUs running for three months, and once deployed, every interaction consumes GPU power and tokens\.

## The Core Components of AI Computing Power Infrastructure

### 1\. Computing Power Hardware: Nvidia DGX H100 AI Server

A standard **Nvidia DGX H100 AI server** \(worth over 2 million RMB\) is a marvel of engineering:

- It houses 8 **Nvidia H100 GPU chips**, each surrounded by 6 SK Hynix HBM high\-bandwidth memory chips using TSMC's top\-tier packaging technology\.

- 4 Nvidia NVSwitch chips enable zero\-latency communication between the GPUs\.

- It also includes 2 Intel Xeon CPUs, 2TB of system memory, and PCIe data lines for data scheduling\.

- High\-speed network cards with optical modules are used for data transmission, and all components are mounted on a high\-performance PCB\.

```plaintext
# Key Components of Nvidia DGX H100
- GPUs: 8 x Nvidia H100
- Memory: 6 x SK Hynix HBM per GPU
- Switches: 4 x Nvidia NVSwitch
- CPUs: 2 x Intel Xeon
- System Memory: 2TB
- Network: High-speed NICs with optical modules
- Carrier: High-performance PCB
```

### 2\. Network Equipment: Switches and Optical Modules

To ensure efficient collaboration among hundreds of thousands of GPUs, network equipment is crucial:

- **Leaf Switches \(Cabinet\-Level\)**: Act as distribution centers, collecting data from the same or adjacent cabinets\. They use multi\-mode \(light blue\) and single\-mode \(yellow\) optical fibers connected via optical modules\.

- **Spine Switches \(Independent\-Level\)**: Aggregate hundreds of leaf switches, connecting countless cabinets into a massive computing cluster\.

### 3\. Cooling and Space: Liquid Cooling

Traditional air cooling limits server density\. Liquid cooling, as seen in Elon Musk's XAI data center, solves this:

- It removes air\-cooling systems, reducing server thickness by half\.

- A single cabinet can now hold 8 servers \(64 H100 chips\), doubling the density and cutting costs for cloud vendors\.

## The Evolution to NVL72: A Paradigm Shift

Nvidia's latest **GB300 NVL72 cabinet** \(mass\-produced in May 2025\) represents a radical redesign:

- **Compute Trays**: Each tray contains Nvidia Grace CPUs, Blackwell GPUs, DPUs \(for security and scheduling\), and ConnectX network cards—all Nvidia\-owned hardware\.

- **NVLink Spine Backplane**: A 70\-pound copper interconnection system that connects 72 GPUs in a cabinet into a single virtual super GPU, eliminating the need for optical modules inside the cabinet\.

- **Switch Trays**: 9 trays with NVLink switch chips enable seamless communication\.

This design pushes Scale\-Up \(physical memory sharing\) to 72 GPUs, reducing latency and increasing bandwidth to 130TB/s\.

## Supply Chain Reconstruction and Competitive Landscape

- **Nvidia's Dominance**: It has evolved from a GPU supplier to a system\-level infrastructure provider\. Cloud vendors must adopt its entire ecosystem, including networks, CPUs, GPUs, and cabinet standards\.

- **Secondary Suppliers**: Other hardware giants have been demoted to secondary or tertiary suppliers, risking obsolescence if they can't keep up with technology\.

## Practical Insights and Opportunities

For businesses and investors, the key is to identify "shovel sellers" in this ecosystem:

- **Chips and Servers**: Nvidia \(GPUs, DPUs\), Intel/AMD \(CPUs\), TSMC \(packaging\)\.

- **Network Equipment**: Cisco, Broadcom \(switches\), Huawei, ZTE \(optical modules\)\.

- **Cooling and Power**: Companies specializing in liquid cooling and high\-power supply systems\.

In conclusion, AI infrastructure is not a bubble but a necessary investment for the next tech revolution\. By understanding the roles and dynamics of each component, you can navigate this landscape and seize opportunities\.

