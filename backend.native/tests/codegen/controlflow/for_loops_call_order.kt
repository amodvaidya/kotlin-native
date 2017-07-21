fun f1(): Int { print("1"); return 0 }
fun f2(): Int { print("2"); return 6 }
fun f3(): Int { print("3"); return 2 }
fun f4(): Int { print("4"); return 3 }

fun main(args: Array<String>) {
    for (i in f1()..f2() step f3() step f4()) { }; println()
    for (i in f1() until f2() step f3() step f4()) {}; println()
    for (i in f2() downTo f1() step f3() step f4()) {}; println()
}