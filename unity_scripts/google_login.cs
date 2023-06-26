using UnityEngine;
using Google;
using System.Threading.Tasks;
using UnityEngine.Networking;

public class GoogleSignInController : MonoBehaviour
{
    public string webClientId;  // Google API Console에서 받은 Web Client ID를 입력해주세요.
    public string serverUrl;   // 여기에 실제 서버 주소를 적어야 합니다.

    private void Start()
    {
        SignInWithGoogle();
    }

    private void SignInWithGoogle()
    {
        GoogleSignIn.Configuration = new GoogleSignInConfiguration
        {
            WebClientId = webClientId,
            RequestIdToken = true
        };

        GoogleSignIn.DefaultInstance.SignIn().ContinueWith(OnGoogleAuthFinished);
    }

    private void OnGoogleAuthFinished(Task<GoogleSignInUser> task)
    {
        if (task.IsFaulted)
        {
            using (IEnumerator<System.Exception> enumerator = task.Exception.InnerExceptions.GetEnumerator())
            {
                if (enumerator.MoveNext())
                {
                    GoogleSignIn.SignInException error = (GoogleSignIn.SignInException)enumerator.Current;
                    Debug.Log("로그인에 실패했습니다. 에러 코드: " + error.Status);
                }
                else
                {
                    Debug.Log("로그인에 실패했습니다. 알 수 없는 에러.");
                }
            }
        }
        else if (task.IsCanceled)
        {
            Debug.Log("로그인이 취소되었습니다.");
        }
        else
        {
            Debug.Log("로그인에 성공했습니다. 사용자 이름: " + task.Result.DisplayName);
            SendTokenToServer(task.Result.IdToken);
        }
    }

    private void SendTokenToServer(string idToken)
    {
        StartCoroutine(SendTokenCoroutine(idToken));
    }

    private IEnumerator SendTokenCoroutine(string idToken)
    {
        WWWForm form = new WWWForm();
        form.AddField("id_token", idToken);

        UnityWebRequest www = UnityWebRequest.Post(serverUrl + "/login_with_token", form);

        yield return www.SendWebRequest();

        if (www.result == UnityWebRequest.Result.ConnectionError || www.result == UnityWebRequest.Result.ProtocolError)
        {
            Debug.Log("서버 요청 에러: " + www.error);
        }
        else
        {
            Debug.Log("서버 응답: " + www.downloadHandler.text);
        }
    }
}
