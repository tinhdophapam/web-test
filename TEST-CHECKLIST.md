# 🧪 Test Checklist - Audio Player

## 🎯 Mục tiêu testing

Đảm bảo Mini Player và Full Player hoạt động đúng trên mọi thiết bị và trình duyệt.

---

## 📱 MOBILE TESTING (≤ 968px)

### Test Case 1: Mini Player Hiển Thị
**Steps:**
1. Mở app trên mobile (hoặc resize browser < 968px)
2. Click vào một bài trong playlist
3. Quan sát mini player ở bottom (phía trên bottom nav)

**Expected Result:**
- ✅ Mini player slide up từ dưới lên (smooth animation)
- ✅ Hiển thị: icon pháp luân, tên bài, thời gian, buttons
- ✅ Progress bar màu cam ở top của mini player
- ✅ Audio bắt đầu phát

**Actual Result:**
- [ ] Pass
- [ ] Fail - Lỗi: _______________

---

### Test Case 2: Click vào Mini Player Info
**Steps:**
1. Đảm bảo mini player đang hiển thị
2. Click vào **icon pháp luân** 🎵

**Expected Result:**
- ✅ Full player modal mở ngay lập tức
- ✅ Full player cover toàn màn hình
- ✅ Mini player biến mất (ẩn đi)
- ✅ Audio tiếp tục phát (không bị ngắt)

**Actual Result:**
- [ ] Pass
- [ ] Fail - Lỗi: _______________

---

### Test Case 3: Click vào Tên Bài
**Steps:**
1. Mini player đang hiển thị
2. Click vào **tên bài** (track title)

**Expected Result:**
- ✅ Full player modal mở
- ✅ Hiển thị đầy đủ thông tin bài hát
- ✅ Audio tiếp tục phát

**Actual Result:**
- [ ] Pass
- [ ] Fail - Lỗi: _______________

---

### Test Case 4: Click vào Thời Gian
**Steps:**
1. Mini player đang hiển thị
2. Click vào **thời gian** (0:00 / 3:45)

**Expected Result:**
- ✅ Full player modal mở

**Actual Result:**
- [ ] Pass
- [ ] Fail - Lỗi: _______________

---

### Test Case 5: Click vào Play/Pause Button
**Steps:**
1. Mini player đang hiển thị, audio đang phát
2. Click vào nút **⏯ Play/Pause**

**Expected Result:**
- ✅ Audio pause/play
- ✅ Icon đổi từ pause → play (hoặc ngược lại)
- ✅ KHÔNG mở full player
- ✅ Vẫn ở trạng thái mini player

**Actual Result:**
- [ ] Pass
- [ ] Fail - Lỗi: _______________

---

### Test Case 6: Click vào Previous/Next Buttons
**Steps:**
1. Mini player đang hiển thị
2. Click vào nút **⏮ Previous** hoặc **⏭ Next**

**Expected Result:**
- ✅ Chuyển sang bài trước/sau
- ✅ Tên bài update
- ✅ KHÔNG mở full player
- ✅ Vẫn ở mini player

**Actual Result:**
- [ ] Pass
- [ ] Fail - Lỗi: _______________

---

### Test Case 7: Click vào Close Button
**Steps:**
1. Mini player đang hiển thị
2. Click vào nút **✕ Close**

**Expected Result:**
- ✅ Mini player đóng (slide xuống)
- ✅ Audio dừng phát
- ✅ Reset về trạng thái ban đầu

**Actual Result:**
- [ ] Pass
- [ ] Fail - Lỗi: _______________

---

### Test Case 8: Click vào Progress Bar (Seek)
**Steps:**
1. Mini player đang hiển thị
2. Click vào **progress bar** (thanh màu cam ở top)

**Expected Result:**
- ✅ Audio seek đến vị trí click
- ✅ Progress bar update
- ✅ KHÔNG mở full player
- ✅ Vẫn ở mini player

**Actual Result:**
- [ ] Pass
- [ ] Fail - Lỗi: _______________

---

### Test Case 9: Swipe Down để đóng Full Player
**Steps:**
1. Mở full player (click vào mini player info)
2. **Swipe down** từ top (100px đầu tiên)
3. Swipe xuống > 100px

**Expected Result:**
- ✅ Full player có visual feedback (di chuyển theo ngón tay)
- ✅ Opacity giảm dần khi swipe
- ✅ Khi thả tay, full player đóng lại
- ✅ Mini player hiện ra lại
- ✅ Audio tiếp tục phát

**Actual Result:**
- [ ] Pass
- [ ] Fail - Lỗi: _______________

---

### Test Case 10: Swipe ngắn (< 100px)
**Steps:**
1. Full player đang mở
2. Swipe down < 100px
3. Thả tay

**Expected Result:**
- ✅ Full player reset về vị trí ban đầu
- ✅ KHÔNG đóng
- ✅ Smooth animation quay về

**Actual Result:**
- [ ] Pass
- [ ] Fail - Lỗi: _______________

---

### Test Case 11: Swipe từ giữa màn hình
**Steps:**
1. Full player đang mở
2. Touch start từ giữa màn hình (> 100px from top)
3. Swipe down

**Expected Result:**
- ✅ Full player KHÔNG đóng
- ✅ Content scroll bình thường
- ✅ Không có visual feedback đóng player

**Actual Result:**
- [ ] Pass
- [ ] Fail - Lỗi: _______________

---

### Test Case 12: Touch Cancel (Interrupt)
**Steps:**
1. Full player đang mở
2. Bắt đầu swipe down
3. Trong lúc swipe, có cuộc gọi đến / notification

**Expected Result:**
- ✅ Full player reset về vị trí ban đầu
- ✅ Không bị stuck ở trạng thái nửa chừng

**Actual Result:**
- [ ] Pass
- [ ] Fail - Lỗi: _______________

---

## 🖥️ DESKTOP TESTING (> 968px)

### Test Case 13: Desktop Layout
**Steps:**
1. Mở app trên desktop (hoặc resize > 968px)
2. Click vào một bài

**Expected Result:**
- ✅ Full player hiển thị ở center
- ✅ KHÔNG có mini player
- ✅ Sidebar visible bên trái
- ✅ Audio phát

**Actual Result:**
- [ ] Pass
- [ ] Fail - Lỗi: _______________

---

### Test Case 14: Resize Window (Desktop → Mobile)
**Steps:**
1. Bắt đầu ở desktop mode (> 968px)
2. Đang phát nhạc
3. Resize window < 968px

**Expected Result:**
- ✅ Mini player xuất hiện
- ✅ Full player ẩn đi
- ✅ Audio tiếp tục phát (không bị ngắt)

**Actual Result:**
- [ ] Pass
- [ ] Fail - Lỗi: _______________

---

### Test Case 15: Resize Window (Mobile → Desktop)
**Steps:**
1. Bắt đầu ở mobile mode (< 968px)
2. Mini player đang hiển thị
3. Resize window > 968px

**Expected Result:**
- ✅ Mini player biến mất
- ✅ Full player hiển thị ở center
- ✅ Audio tiếp tục phát

**Actual Result:**
- [ ] Pass
- [ ] Fail - Lỗi: _______________

---

## 🌐 CROSS-BROWSER TESTING

### Chrome/Edge (Chromium)
- [ ] All tests pass
- [ ] Notes: _______________

### Firefox
- [ ] All tests pass
- [ ] Notes: _______________

### Safari (Desktop)
- [ ] All tests pass
- [ ] Notes: _______________

### Safari (iOS)
- [ ] All tests pass
- [ ] Notes: _______________

### Samsung Internet
- [ ] All tests pass
- [ ] Notes: _______________

---

## 📊 PERFORMANCE TESTING

### Animation Smoothness
**Steps:**
1. Mở DevTools → Performance tab
2. Click Record
3. Phát nhạc → Mở/đóng full player nhiều lần
4. Stop recording

**Expected Result:**
- ✅ FPS: 60fps (steady green line)
- ✅ No long tasks (> 50ms)
- ✅ No layout thrashing

**Actual Result:**
- FPS: _____ fps
- Long tasks: _____ ms
- [ ] Pass
- [ ] Fail - Lỗi: _______________

---

### Touch Response Time
**Steps:**
1. Trên mobile
2. Click vào mini player info
3. Đo thời gian từ touch → full player hiện

**Expected Result:**
- ✅ < 50ms (instant)

**Actual Result:**
- Response time: _____ ms
- [ ] Pass
- [ ] Fail

---

### Memory Leaks
**Steps:**
1. Mở DevTools → Memory tab
2. Take snapshot
3. Phát 10 bài liên tiếp
4. Mở/đóng full player 20 lần
5. Take snapshot lại
6. Compare

**Expected Result:**
- ✅ Memory increase < 5MB
- ✅ No detached DOM nodes

**Actual Result:**
- Memory increase: _____ MB
- Detached nodes: _____
- [ ] Pass
- [ ] Fail

---

## 🔊 AUDIO TESTING

### Test Case 16: Audio không bị ngắt khi switch view
**Steps:**
1. Phát nhạc trên mobile
2. Mini player → Full player
3. Full player → Mini player (swipe down)
4. Lặp lại 5 lần

**Expected Result:**
- ✅ Audio phát liên tục, không bị ngắt
- ✅ Không có glitch/stutter
- ✅ Progress bar update đều

**Actual Result:**
- [ ] Pass
- [ ] Fail - Lỗi: _______________

---

### Test Case 17: Seek chính xác
**Steps:**
1. Phát nhạc
2. Click vào progress bar ở vị trí 50%

**Expected Result:**
- ✅ Audio seek đến đúng vị trí 50%
- ✅ Time display update đúng

**Actual Result:**
- [ ] Pass
- [ ] Fail - Lỗi: _______________

---

## 📱 DEVICE-SPECIFIC TESTING

### iPhone (Safari iOS)
- Screen size: _____
- iOS version: _____
- [ ] All tests pass
- Issues: _______________

### Android (Chrome)
- Screen size: _____
- Android version: _____
- [ ] All tests pass
- Issues: _______________

### Android (Samsung Internet)
- Screen size: _____
- Android version: _____
- [ ] All tests pass
- Issues: _______________

### iPad (Safari)
- Screen size: _____
- iOS version: _____
- [ ] All tests pass
- Issues: _______________

---

## 🐛 EDGE CASES

### Test Case 18: Orientation Change
**Steps:**
1. Phát nhạc ở portrait mode
2. Rotate sang landscape
3. Rotate về portrait

**Expected Result:**
- ✅ UI adapt smooth
- ✅ Audio không bị ngắt
- ✅ Mini/Full player vẫn hoạt động

**Actual Result:**
- [ ] Pass
- [ ] Fail - Lỗi: _______________

---

### Test Case 19: Slow Network
**Steps:**
1. DevTools → Network → Slow 3G
2. Click vào một bài

**Expected Result:**
- ✅ Loading indicator hiển thị
- ✅ Mini player vẫn hiện (có thể show loading state)
- ✅ Khi loaded, audio phát bình thường

**Actual Result:**
- [ ] Pass
- [ ] Fail - Lỗi: _______________

---

### Test Case 20: Offline
**Steps:**
1. Phát nhạc
2. Disconnect network
3. Try to play another track

**Expected Result:**
- ✅ Error message rõ ràng
- ✅ Track hiện tại vẫn phát (nếu đã buffer)

**Actual Result:**
- [ ] Pass
- [ ] Fail - Lỗi: _______________

---

## ✅ SUMMARY

**Total Tests:** 20
**Passed:** _____ / 20
**Failed:** _____ / 20
**Pass Rate:** _____ %

**Critical Issues:**
1. _______________
2. _______________
3. _______________

**Minor Issues:**
1. _______________
2. _______________

**Browser Compatibility:**
- Chrome: [ ] Pass [ ] Fail
- Firefox: [ ] Pass [ ] Fail
- Safari: [ ] Pass [ ] Fail
- Mobile: [ ] Pass [ ] Fail

**Recommendation:**
- [ ] ✅ Ready for Production
- [ ] ⚠️ Need Fixes Before Deploy
- [ ] ❌ Major Issues, Do Not Deploy

---

**Tester:** _______________
**Date:** _______________
**Version:** 1.1.0
**Notes:** _______________
