function checkFlag() {
    var correct_flag = "flag{dz13n_0tw@rty_UG}"
    var given_flag = document.getElementById("fname").value;

    if (given_flag == correct_flag) {
        document.getElementById("msg").innerHTML = "Poprawna flaga, gratuluje!";
        return true;
    }
}
