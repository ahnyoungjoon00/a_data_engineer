const renderTime = () => {
    const now = new Date();
    const hours = now.getHours().toString();
    const minutes = now.getMinutes().toString();
    const seconds = now.getSeconds().toString();

    // 시분초값이 1자리라면 앞에 0을 채우는 함수를 사용 (padding)
    const text = `${hours}:${minutes}:${seconds}`
    clockText.textContent = text;
    return;
}

renderTime();
setInterval(renderTime, 1000);