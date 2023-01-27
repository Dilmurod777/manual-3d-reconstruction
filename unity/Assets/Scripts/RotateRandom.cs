using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class RotateRandom : MonoBehaviour
{
    public bool xAxis = true;
    public bool yAxis = false;
    public bool zAxis = false;

    public float xSpeed = 15.0f;
    public float ySpeed = 15.0f;
    public float zSpeed = 15.0f;

    private void Update()
    {
        transform.Rotate(
            (xAxis ? 1 : 0) * xSpeed * Time.deltaTime,
            (yAxis ? 1 : 0) * ySpeed * Time.deltaTime,
            (zAxis ? 1 : 0) * zSpeed * Time.deltaTime);
    }
}