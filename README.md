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


## 1. Basic COCOMO Model
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

The constant values **a,b,c,** and **d** for the Basic Model for the different categories of the system are :<br>
![basic cocomo](https://user-images.githubusercontent.com/73381366/194706141-ebc6f551-5600-4616-902b-1dccc5ff41d1.jpg)

## 2. Intermediate COCOMO Model
Intermediate COCOMO model is an extension of the Basic COCOMO model which includes a set of cost drivers into account in order to enhance more accuracy to the cost estimation model as a result. 
<br><br>
![equation](https://latex.codecogs.com/svg.image?E&space;=&space;a*(KLOC)^{b}&space;*(EAF))
<br>
![equation](https://latex.codecogs.com/svg.image?D&space;=&space;c*(E)^{d}) 
<br>
![equation](https://latex.codecogs.com/svg.image?P&space;=&space;E/D)

where,<br>
**EAF** is the Effort Adjustment Factor, which is calculated by multiplying the parameter values of different cost driver parameters.. <br>
**E** is **effort** applied in person-months.<br>
**D** is development **time** in months.<br>
**P** is the **total no. of persons** required to accomplish the project.
<br>

The parameters for calculating EAF are :<br>
![parameters cocomo](https://user-images.githubusercontent.com/73381366/194706653-13cc7d5f-4a60-413b-9718-4d89ca7bd1e5.jpg)

<br><br><br>
The constant values **a,b,c,** and **d** for the Intermediate Model for the different categories of the system are :<br>
![inter cocomo](https://user-images.githubusercontent.com/73381366/194706602-f79eac37-755d-4631-8c24-1c7ec8fbdd46.jpg)
<br><br>

## 3. Advanced COCOMO Model

The model incorporates all qualities of both Basic COCOMO and Intermediate COCOMO strategies on each software engineering process.<br> 
The model accounts for the influence of the individual development phase (analysis, design, etc.) of the project, it uses multipliers for each phase of the project , it includes more factors that influence the software projects and gives more accurate estimations. <br>

The **six phases** of advanced COCOMO are:

1. Planning and requirements
2. System design
3. Detailed design
4. Module code and test
5. Integration and test
6. Cost Constructive model

