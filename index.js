function getRepos() {
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("input");
  filter = input.value.toUpperCase();
  table = document.getElementById("repoTable");
  tr = table.getElementsByTagName("tr");

  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[0];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}

function copyToClipboard(name) {
  navigator.clipboard.writeText(name);
  alert("Name copied. You can now search " + name + " on slack.");
}

function showSteps() {
  stepsBox = document.getElementById("steps");
  overlayFlex = document.getElementById("hidden-flex");
  
  stepsBox.style.display = "flex";
  overlayFlex.style.display = "flex";

}

function hideSteps() {
  stepsBox = document.getElementById("steps");
  overlayFlex = document.getElementById("hidden-flex");

  stepsBox.style.display = "none";
  overlayFlex.style.display = "none";
}
  