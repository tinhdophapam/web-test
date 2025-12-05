# iOS Audio Playback Fix

## Vấn đề
Audio từ GitHub releases không phát được trên iPhone (iOS Safari)

## Nguyên nhân
1. **GitHub Redirects**: GitHub releases redirect qua nhiều URL trước khi đến file thực, iOS Safari không xử lý tốt redirects cho audio
2. **CORS Issues**: Safari iOS rất nghiêm ngặt với CORS
3. **Autoplay Policy**: iOS yêu cầu user interaction trước khi phát audio
4. **Preload**: iOS không hỗ trợ tốt `preload="metadata"`

## Các thay đổi đã thực hiện

### 1. HTML (index.html)
- Thay đổi `preload="metadata"` thành `preload="none"` 
- Thêm `crossorigin="anonymous"` cho audio element

### 2. JavaScript (app.js)

#### a. iOS Audio Unlock
- Thêm function `setupIOSAudioUnlock()` để unlock audio context khi user tương tác lần đầu
- iOS yêu cầu user interaction để phát audio

#### b. GitHub URL Resolution
- Thêm function `resolveGitHubUrl()` để resolve GitHub release URLs
- Sử dụng `fetch()` với `HEAD` request để lấy URL thực sau redirects
- GitHub redirect đến CDN URL hoạt động tốt hơn trên iOS

#### c. Improved Error Handling
- Thêm error messages cụ thể cho iOS
- Detect iOS device và hiển thị thông báo phù hợp
- Better promise handling cho audio.play()

#### d. Explicit Audio Loading
- Gọi `audio.load()` trước khi play
- Cải thiện compatibility với iOS Safari

#### e. Event Listeners
- Thêm `canplaythrough`, `waiting`, `stalled` events
- Better tracking của audio loading state

## Cách test
1. Mở website trên iPhone Safari
2. Chọn một bài giảng từ GitHub releases
3. Audio sẽ tự động resolve URL và phát

## Lưu ý
- Lần đầu tiên user phải tương tác (click/touch) để unlock audio
- Nếu GitHub URL vẫn fail, sẽ tự động fallback sang backupUrl (Google Drive)
- Console logs sẽ hiển thị quá trình resolve URL

## Backup URLs
Nếu GitHub URL không hoạt động, app sẽ tự động thử backupUrl (Google Drive links) đã có sẵn trong lectures.json
