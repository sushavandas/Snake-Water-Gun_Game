function makeChoice(choice) {
    eel.play(choice)(function(response) {
        document.getElementById("output").innerHTML =
            "You chose: " + response.user_choice +
            "<br>Computer chose: " + response.computer_choice +
            "<br><b>" + response.result + "</b>";
    });
}
