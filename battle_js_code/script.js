let livee = 10000;
let live_Boss = 25000;
let patron = 35;
document.getElementById("live").innerHTML = "Your xp: " + livee;
document.getElementById("live_boss").innerHTML = "Boss xp: " + live_Boss;
document.getElementById("patrons").innerHTML = "Cartridges: " + patron;
function snake_() {
  const audio = new Audio('popadanie-puli-v-tsel-i-padenie.mp3');
  audio.autoplay = true;
  patron--;
}
function ydar() {
  const audio = new Audio('pistolet-vystrel-6.mp3');
  audio.autoplay = true;
  patron--;
  live_Boss = live_Boss - 1000;
}
var intervalId = setInterval(patrons, 1000);
var atack_ = setInterval(atack, 9000);
function patrons() {
  document.getElementById("live").innerHTML = "Your xp: " + livee;
  document.getElementById("patrons").innerHTML = "Cartridges: " + patron;
  document.getElementById("live_boss").innerHTML = "Boss xp: " + live_Boss;
  if (patron <= 0 ) {
    document.getElementById("first_Boss").hidden = true;
    document.getElementById("end").innerHTML = "Game Over! Lol <br> I can say Breme" ;
    clearInterval(intervalId);
    clearInterval(atack_);
    const audio = new Audio('undertale-game-over-theme-(128-kbps)-by-voicemod.mp3');
    audio.autoplay = true;
    }
    if (livee <= 0 ) {
      document.getElementById("first_Boss").hidden = true;
      document.getElementById("end").innerHTML = "Game Over! Lol <br> Bruh" ;
      clearInterval(intervalId);
      const audio = new Audio('undertale-game-over-theme-(128-kbps)-by-voicemod.mp3');
      audio.autoplay = true;
      clearInterval(atack_);
      }
      if (live_Boss <= 0) {
        document.getElementById("first_Boss").hidden = true;
      document.getElementById("end").innerHTML = "You win!!<br> You cool, thaks" ;
      clearInterval(intervalId);
      clearInterval(atack_);
      const audio = new Audio('y2mate.com - RXDXVIL  Bad Pigges Phonk.mp3');
      audio.autoplay = true;
      }
}

function atack() {
 livee = livee - 1000;
 const audio = new Audio('shipenie-zmei.mp3');
      audio.autoplay = true;
}