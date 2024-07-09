let flashes = document.getElementsByClassName("flash-message-button");

for (let flash of flashes) {
    flash.addEventListener("click", () => {
        let parent = flash.parentElement;        
        parent.remove();
    });
}
