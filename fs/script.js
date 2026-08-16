// Creating Student class
class Student {
    constructor(name, rollNo, department, cgpa) {
        this.name = name;
        this.rollNo = rollNo;
        this.department = department;
        this.cgpa = cgpa;
    }
}

// Selecting button and profile container
const createBtn = document.getElementById("createBtn");
const profileContainer = document.getElementById("profileContainer");

// Event handling
createBtn.addEventListener("click", function () {

    // Getting user-provided values
    const name = document.getElementById("name").value;
    const rollNo = document.getElementById("rollNo").value;
    const department = document.getElementById("department").value;
    const cgpa = document.getElementById("cgpa").value;

    // Creating Student object
    const student = new Student(name, rollNo, department, cgpa);

    // Creating profile dynamically
    const profile = document.createElement("div");
    profile.className = "profile";

    const heading = document.createElement("h2");
    heading.textContent = "Student Profile";

    const namePara = document.createElement("p");
    namePara.textContent = "Name : " + student.name;

    const rollPara = document.createElement("p");
    rollPara.textContent = "Roll No : " + student.rollNo;

    const deptPara = document.createElement("p");
    deptPara.textContent = "Department : " + student.department;

    const cgpaPara = document.createElement("p");
    cgpaPara.textContent = "CGPA : " + student.cgpa;

    // Adding elements to profile
    profile.appendChild(heading);
    profile.appendChild(namePara);
    profile.appendChild(rollPara);
    profile.appendChild(deptPara);
    profile.appendChild(cgpaPara);

    // Displaying profile on webpage
    profileContainer.innerHTML = "";
    profileContainer.appendChild(profile);
});