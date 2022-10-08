# COCOMO-Calculator

### About COCOMO

COCOMO stands for **CO**nstructive **CO**st **MO**del. <br>
It is  is used to estimate the development efforts which are involved in a project. COCOMO is based upon the estimation of lines of code in a system and the time.

 COCOMO model strategies are classified into 3 categories:
 - Organic -> That is when project is small and simple and the team is small with prior experience.
 - Semi-detached -> When project has complexity and team requires more experience, better guidance and creativity.
 - Embedded -> It is when project has fixed requirements of resources and product is developed within very tight constraints.

<br>

**Types of COCOMO Models**
- Basic
- Intermediate
- Advanced


### 1. Basic COCOMO Model
 The Basic COCOMO Model can be used for quick and slightly rough calculations of Software Costs since the model considers the lines of code mainly along with constant values obtained from software project types.
 
The estimation is given by: <br><br>
![equation](https://latex.codecogs.com/svg.image?E&space;=&space;a*(KLOC)^{b}) 
<br>
![equation](https://latex.codecogs.com/svg.image?D&space;=&space;c*(E)^{d}) 
<br>
![equation](https://latex.codecogs.com/svg.image?P&space;=&space;E/D)
<br><br>
where,<br>
**E** is **effort** applied in person-months.<br>
**D** is development **time** in months.<br>
**P** is the **total no. of persons** required to accomplish the project.
<br>

The constant values **a,b,c,** and **d** for the Basic Model for the different categories of the system are :
![basic cocomo](https://user-images.githubusercontent.com/73381366/194706141-ebc6f551-5600-4616-902b-1dccc5ff41d1.jpg)


