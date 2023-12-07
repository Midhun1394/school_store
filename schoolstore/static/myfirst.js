var mealsByCategory = {
  A: ["Bsc", "Msc", "Computer Science Engineering", "Diploma in computer science", "Others"],
  B: ["Bcom", "", "Accounting", "Bca", "Others"],
  C: ["Sociology", "Political Science", "Others"],
  D: ["Bsc", "Msc", "Others"],
  E: ["Mbbs", "Microbiology", "Biochemistry", "Others"],
}

function changecat(value) {
  if (value.length == 0) document.getElementById("category").innerHTML = "<option></option>";
  else {
    var catOptions = "";
    for (categoryId of mealsByCategory[value]) {
      catOptions += "<option>" + categoryId + "</option>";
    }
    document.getElementById("category").innerHTML = catOptions;
  }
}