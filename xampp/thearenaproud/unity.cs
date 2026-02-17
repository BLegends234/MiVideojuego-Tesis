using System.Collections;
using UnityEngine;
using UnityEngine.Networking;

public class ApiHandler : MonoBehaviour
{
    IEnumerator SendDataToApi(string url, string jsonData)
    {
        UnityWebRequest request = new UnityWebRequest(url, "POST");
        byte[] jsonToSend = new System.Text.UTF8Encoding().GetBytes(jsonData);
        
        request.uploadHandler = new UploadHandlerRaw(jsonToSend);
        request.downloadHandler = new DownloadHandlerBuffer();
        request.SetRequestHeader("Content-Type", "application/json");

        yield return request.SendWebRequest();

        if (request.result == UnityWebRequest.Result.ConnectionError || request.result == UnityWebRequest.Result.ProtocolError)
        {
            Debug.LogError("Error: " + request.error);
        }
        else
        {
            Debug.Log("Datos enviados exitosamente: " + request.downloadHandler.text);
        }
    }

    // Método para llamar al envío de datos
    public void SendData()
    {
        string url = "http://127.0.0.1:8000/user/";
        string jsonData = "{\"key\": \"value\"}";  // JSON de ejemplo
        StartCoroutine(SendDataToApi(url, jsonData));
    }
}