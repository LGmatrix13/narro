document.addEventListener("DOMContentLoaded", async () => {
    const noun1 = document.getElementById("noun1");

    const noun2 = document.getElementById("noun2");
    noun2.hidden = true;

    const noun3 = document.getElementById("noun3");
    noun3.hidden = true;

    const noun4 = document.getElementById("noun4");
    noun4.hidden = true;

    const noun5 = document.getElementById("noun5");
    noun5.hidden = true;

    const nounButton = document.getElementById("add-noun");

    const adjective1 = document.getElementById("adjective1");

    const adjective2 = document.getElementById("adjective2");
    adjective2.hidden = true;

    const adjective3 = document.getElementById("adjective3");
    adjective3.hidden = true;

    const adjectiveButton = document.getElementById("add-adjective");

    const verb1 = document.getElementById("verb1");

    const verb2 = document.getElementById("verb2");
    verb2.hidden = true;

    const verb3 = document.getElementById("verb3");
    verb3.hidden = true;

    const verb4 = document.getElementById("verb4");
    verb4.hidden = true;

    const verbButton = document.getElementById("add-verb");


    nounButton.addEventListener("click", () => {
        if(noun2.hidden == true){
            noun2.hidden=false;
        } else if(noun3.hidden == true){
            noun3.hidden = false;
        }else if(noun4.hidden == true){
            noun4.hidden = false;
        }else{
            noun5.hidden = false;
            nounButton.hidden = true;
        }
    })

    adjectiveButton.addEventListener("click", () => {
        if(adjective2.hidden == true){
            adjective2.hidden=false;
        }else{
            adjective3.hidden = false;
            adjectiveButton.hidden = true;
        }
    })

    verbButton.addEventListener("click", () => {
        if(verb2.hidden == true){
            verb2.hidden=false;
        } else if(verb3.hidden == true){
            verb3.hidden = false;
        }else{
            verb4.hidden = false;
            verbButton.hidden = true;
        }
    })
})