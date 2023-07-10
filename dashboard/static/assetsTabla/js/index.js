

const listProgrammers = async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/listaAlumno/");
        
        }
     catch (ex) {
        alert(ex);
    }
};

window.addEventListener("load", async () => {
    await initDataTable();
});