function main() {
    let a = 2;
    let b = 3;
    let c = 2;
    if (a <= 0 || b <= 0 || c <= 0) {
        console.log("Erro: Valores devem ser maiores que zero");
    } else {
        if ((a + b > c) && (a + c > b) && (b + c > a)) {
            if (a == b && b == c) {
                console.log("Triângulo equilátero válido");
            } else if (a == b || a == c || b == c) {
                console.log("Triângulo isósceles válido");
            } else {
                console.log("Triângulo escaleno válido");
            }
        } else {
            console.log("Medidas inválidas");
        }
    }
}

main();