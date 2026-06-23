function main() {
    let i = 1;
    let acumulador = 0;
    while (i <= 4) {
        acumulador = acumulador + i;
        i = i + 1;
    }
    console.log("Total acumulado do loop:");
    console.log(acumulador);
}

main();