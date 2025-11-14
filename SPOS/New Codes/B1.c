#include <jni.h>
#include <stdio.h>
#include "B1.h"

JNIEXPORT jint JNICALL Java_B1_add(JNIEnv *env, jobject obj, jint a, jint b) {
    jint result = a + b;
    printf("\n%d + %d = %d\n", a, b, result);
    return result;
}

JNIEXPORT jint JNICALL Java_B1_sub(JNIEnv *env, jobject obj, jint a, jint b) {
    jint result = a - b;
    printf("\n%d - %d = %d\n", a, b, result);
    return result;
}

JNIEXPORT jint JNICALL Java_B1_mult(JNIEnv *env, jobject obj, jint a, jint b) {
    jint result = a * b;
    printf("\n%d * %d = %d\n", a, b, result);
    return result;
}

JNIEXPORT jint JNICALL Java_B1_div(JNIEnv *env, jobject obj, jint a, jint b) {
    if (b != 0) {
        jint result = a / b;
        printf("\n%d / %d = %d\n", a, b, result);
        return result;
    } else {
        printf("\nError: Division by zero\n");
        return 0; // Or another appropriate error value
    }
}
