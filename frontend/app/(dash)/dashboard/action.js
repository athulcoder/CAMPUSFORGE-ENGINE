export async function uploadResume(file, onProgress) {


return new Promise( async(resolve, reject) => {
    const xhr = new XMLHttpRequest();
    const formData = new FormData();
    formData.append("file", file);

    xhr.upload.onprogress = (e) => {
      if (e.lengthComputable) {
        const percent = Math.round((e.loaded / e.total) * 100);
        onProgress(percent);
      }
    };

    xhr.onload = () => {
      if (xhr.status === 201) {
        resolve(JSON.parse(xhr.responseText));
      } else {
        reject(xhr.responseText);
      }
    };

    xhr.onerror = reject;

    xhr.open("POST", `${process.env.NEXT_PUBLIC_BASE_URL}/api/resume/upload`);
    xhr.withCredentials = true;
    xhr.send(formData);
  });
}