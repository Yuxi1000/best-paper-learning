# Appendix/other: Generating Physically Stable and Buildable Brick Structures from Text

- id: `brickgpt`
- source: arXiv:2505.05469

## B. Robotic Assembly

We demonstrate automated assembly using a dual-robot- arm system as shown in Figure 10. The system consists of two Yaskawa GP4 robots, each equipped with an ATI force-torque sensor. A calibrated baseplate is placed between them, and the robots use the bricks initially placed on the plate to construct the brick structure. Given a brick struc- ture B = [b1, b2, . . . , bN], we employ the action mask in [40] with assembly-by-disassembly search [73] to generate a physically executable assembly sequence for the robots, i.e., reordering the brick sequence so that 1) each intermediate structure is physically stable by itself, 2) each intermediate structure is stable under the robot operation, and 3) each as- sembly step is executable within the system’s dexterity. With the executable assembly sequence, an asynchronous planner [24] distributes the assembly tasks to the robots, plans the robots’ movements, and coordinates the bimanual system to construct the brick structure. The robots use the end-of-arm tool and the manipulation policy presented in [24, 39] with closed-loop force control to robustly manipulate bricks and construct the structure.

## C. Manual Assembly

As shown in Figure 11, human users can assemble our gen- erated structures, demonstrating their physical stability and buildability. Notably, since our method outputs a sequence of intermediate steps, it naturally serves as an intuitive as- sembly guide. … … … … … … Figure 10. Automated Assembly. We demonstrate robotic assembly of generated structures using LEGO bricks.
