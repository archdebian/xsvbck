from fastapi import FastAPI, Header, HTTPException
import yt_dlp
import uvicorn
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "SaveX is Running!"}

@app.get("/tiktok")
async def get_tiktok_video(url: str, user_agent: str = Header(default=None)):
    if not url:
        raise HTTPException(status_code=400, detail="URL is required")

    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'no_warnings': True,
        # User Agent sangat penting agar tidak terdeteksi bot
        'user_agent': user_agent if user_agent else 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return {
                "status": "success",
                "title": info.get('title'),
                "thumbnail": info.get('thumbnail'),
                "download_url": info.get('url') 
            }
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
