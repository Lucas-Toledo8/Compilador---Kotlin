fun main() {
    var n: Int = 5;
    var i: Int = 0;

    println("Gerando Triangulo de Pascal:");
    println("");

    while (i < n) {
        var j: Int = 0;
        var num: Int = 1;
        
        while (j <= i) {
            println(num); 
            num = num * (i - j) / (j + 1);
            j = j + 1;
        }
        
        println("");
        i = i + 1;
    }
}