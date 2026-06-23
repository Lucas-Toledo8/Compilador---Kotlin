fun main(){
    var i = 1;
    var acumulador = 0;
    while (i <= 4) {
        acumulador = acumulador + i; // 0+1, 1+2, 3+3, 6+4 = 10
        i = i + 1;
    }
    println("Total acumulado do loop:");
    println(acumulador);
}
