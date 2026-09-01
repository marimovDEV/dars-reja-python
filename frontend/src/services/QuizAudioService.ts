class QuizAudioService {
  private ctx: AudioContext | null = null;
  private isMuted: boolean = false;
  private volume: number = 0.5;

  private initCtx() {
    if (!this.ctx) {
      const AudioCtxClass = window.AudioContext || (window as any).webkitAudioContext;
      if (AudioCtxClass) {
        this.ctx = new AudioCtxClass();
      }
    }
    if (this.ctx && this.ctx.state === 'suspended') {
      this.ctx.resume();
    }
  }

  public setMuted(muted: boolean) {
    this.isMuted = muted;
  }

  public setVolume(vol: number) {
    this.volume = Math.max(0, Math.min(1, vol));
  }

  public getMuted(): boolean {
    return this.isMuted;
  }

  // Play short synthesized beep
  private playTone(freq: number, durationSec: number, type: OscillatorType = 'sine', delaySec: number = 0) {
    if (this.isMuted) return;
    try {
      this.initCtx();
      if (!this.ctx) return;

      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();

      osc.type = type;
      osc.frequency.setValueAtTime(freq, this.ctx.currentTime + delaySec);

      gain.gain.setValueAtTime(this.volume * 0.3, this.ctx.currentTime + delaySec);
      gain.gain.exponentialRampToValueAtTime(0.0001, this.ctx.currentTime + delaySec + durationSec);

      osc.connect(gain);
      gain.connect(this.ctx.destination);

      osc.start(this.ctx.currentTime + delaySec);
      osc.stop(this.ctx.currentTime + delaySec + durationSec);
    } catch (e) {
      console.warn("Audio play error:", e);
    }
  }

  // 1. Countdown Tick (last 5 seconds)
  public playTick() {
    this.playTone(800, 0.1, 'sine');
  }

  // 2. Question Start Chime
  public playQuestionStart() {
    this.playTone(523.25, 0.12, 'triangle', 0.0); // C5
    this.playTone(659.25, 0.12, 'triangle', 0.1); // E5
    this.playTone(783.99, 0.20, 'triangle', 0.2); // G5
  }

  // 3. Correct Answer (Ding ✨)
  public playCorrect() {
    this.playTone(587.33, 0.15, 'sine', 0.0); // D5
    this.playTone(880.00, 0.35, 'sine', 0.1); // A5
  }

  // 4. Incorrect Answer (Buzz ❌)
  public playIncorrect() {
    this.playTone(164.81, 0.25, 'sawtooth', 0.0); // E3
    this.playTone(130.81, 0.35, 'sawtooth', 0.15); // C3
  }

  // 5. Fanfare / Victory Podium
  public playFanfare() {
    const notes = [
      { f: 523.25, d: 0.15, t: 0.0 }, // C5
      { f: 659.25, d: 0.15, t: 0.15 }, // E5
      { f: 783.99, d: 0.15, t: 0.30 }, // G5
      { f: 1046.50, d: 0.60, t: 0.45 } // C6
    ];
    notes.forEach(n => this.playTone(n.f, n.d, 'triangle', n.t));
  }
}

export const quizAudio = new QuizAudioService();
