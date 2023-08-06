use std::time::Duration;

use pyo3::prelude::*;
use songbird::tracks::{LoopState, PlayMode, TrackHandle, TrackResult, TrackState};
use std::sync::Arc;

use crate::event::{EventHanlder, PyEvent};
use crate::exceptions::TrackError;
use crate::utils::unwrap_duration;

pub fn handle_track_result<'p, T>(res: TrackResult<T>) -> Result<T, PyErr> {
    match res {
        Ok(t) => Ok(t),
        Err(err) => Err(TrackError::new_err(format!("{:?}", err))),
    }
}

#[allow(dead_code)]
#[pyclass(name = "PlayMode")]
#[derive(Clone)]
pub struct PyPlayMode {
    play_mode: PlayMode,
}

/// The current state of the track. ie. Paused/Unpaused.
impl PyPlayMode {
    pub fn from(play_mode: PlayMode) -> Self {
        Self { play_mode }
    }
}

#[allow(non_snake_case)]
#[pymethods]
impl PyPlayMode {
    #[classattr]
    fn Play() -> Self {
        Self::from(PlayMode::Play)
    }
    #[classattr]
    fn Pause() -> Self {
        Self::from(PlayMode::Pause)
    }
    #[classattr]
    fn Stop() -> Self {
        Self::from(PlayMode::Stop)
    }
    #[classattr]
    fn End() -> Self {
        Self::from(PlayMode::End)
    }
}

#[allow(dead_code)]
#[pyclass(name = "LoopCount")]
#[derive(Clone)]
pub struct PyLoopState {
    #[pyo3(get, set)]
    loop_state: Option<usize>,
}

impl PyLoopState {
    pub fn from(loop_state: LoopState) -> Self {
        Self {
            loop_state: match loop_state {
                LoopState::Finite(n) => Some(n),
                LoopState::Infinite => None,
            },
        }
    }
    pub fn from_usize(n: Option<usize>) -> Self {
        Self { loop_state: n }
    }
    #[allow(dead_code)]
    pub fn as_songbird_loop_state(&self) -> LoopState {
        match self.loop_state {
            Some(usize) => LoopState::Finite(usize),
            None => LoopState::Infinite,
        }
    }
}

/// The state of the track.
#[pyclass(name = "TrackState")]
pub struct PyTrackState {
    #[pyo3(get, set)]
    playing: PyPlayMode,
    #[pyo3(get, set)]
    volume: f32,
    #[pyo3(get, set)]
    position: f64,
    #[pyo3(get, set)]
    play_time: f64,
    #[pyo3(get, set)]
    loops: PyLoopState,
}

impl PyTrackState {
    pub fn from(track_state: TrackState) -> Self {
        Self {
            playing: PyPlayMode::from(track_state.playing),
            volume: track_state.volume,
            position: track_state.position.as_secs_f64(),
            play_time: track_state.play_time.as_secs_f64(),
            loops: PyLoopState::from(track_state.loops),
        }
    }
}

/// The metadata for a track
///
/// Attributes
/// ----------
/// track
///     The track of this stream.
/// artist
///     The main artist of the track.
/// data
///     The date of creation of the stream.
/// channels
///     The number of audio channels in the track. Any number >= 2 is treated as stereo.
/// channel
///     The youtube channel for the track.
/// start_time
///     The time at which playback was started.
/// source_url
///     The source url of the stream.
/// title
///     The YouTube title of the track.
/// thumbnail
///     The thumbnail url of this stream.
#[pyclass(name = "Metadata")]
pub struct PyMetadata {
    #[pyo3(get)]
    track: Option<String>,
    #[pyo3(get)]
    artist: Option<String>,
    #[pyo3(get)]
    date: Option<String>,
    #[pyo3(get)]
    channels: Option<u8>,
    #[pyo3(get)]
    channel: Option<String>,
    #[pyo3(get)]
    start_time: Option<f64>,
    #[pyo3(get)]
    duration: Option<f64>,
    #[pyo3(get)]
    sample_rate: Option<u32>,
    #[pyo3(get)]
    source_url: Option<String>,
    #[pyo3(get)]
    title: Option<String>,
    #[pyo3(get)]
    thumbnail: Option<String>,
}

#[pyclass(name = "TrackHandle")]
pub struct PyTrackHandle {
    track_handle: Arc<TrackHandle>,
}

/// Used to control a track that is already playing. None of the methods are async.
impl PyTrackHandle {
    pub fn from(track_handle: TrackHandle) -> Self {
        Self {
            track_handle: Arc::from(track_handle),
        }
    }
}

#[pymethods]
impl PyTrackHandle {
    /// Stops the track from playing.
    #[pyo3(text_signature = "($self)")]
    fn play(&self) -> PyResult<()> {
        handle_track_result(self.track_handle.play())
    }
    /// Unpauses the track.
    #[pyo3(text_signature = "($self)")]
    fn pause(&self) -> PyResult<()> {
        handle_track_result(self.track_handle.pause())
    }
    /// Stops the track. A track stopped with Stop cannot be restarted.
    #[pyo3(text_signature = "($self)")]
    fn stop(&self) -> PyResult<()> {
        handle_track_result(self.track_handle.pause())
    }
    /// Sets the volume of the track.
    #[pyo3(text_signature = "($self, volume)")]
    fn set_volume(&self, volume: f32) -> PyResult<()> {
        handle_track_result(self.track_handle.set_volume(volume))
    }
    /// Makes a lazily initialized track playable. This does not matter to the current
    /// functionality of the lib because ``Restartable`` is not implemented.
    #[pyo3(text_signature = "($self)")]
    fn make_playable(&self) -> PyResult<()> {
        handle_track_result(self.track_handle.make_playable())
    }
    #[getter]
    fn is_seekable(&self) -> bool {
        self.track_handle.is_seekable()
    }
    /// Seeks to a specific time in the track.
    #[pyo3(text_signature = "($self)")]
    fn seek_time(&self, position: f64) -> PyResult<()> {
        handle_track_result(
            self.track_handle
                .seek_time(Duration::from_secs_f64(position)),
        )
    }
    /// Adds an event to the track.
    #[pyo3(text_signature = "($self)")]
    fn add_event(&self, py: Python, event: &PyEvent, call: PyObject) -> PyResult<()> {
        let current_loop = pyo3_asyncio::get_running_loop(py)?;
        handle_track_result(self.track_handle.add_event(
            event.event,
            EventHanlder::new(call, PyObject::from(current_loop)),
        ))
    }
    /// Gets the `TrackState` for a track.
    #[pyo3(text_signature = "($self)")]
    fn get_info<'p>(&'p self, py: Python<'p>) -> PyResult<&'p PyAny> {
        let track_handle = self.track_handle.clone();

        pyo3_asyncio::tokio::future_into_py(py, async move {
            let track_state = handle_track_result(track_handle.get_info().await)?;
            Ok(PyTrackState::from(track_state))
        })
    }
    /// Enables looping.
    #[pyo3(text_signature = "($self)")]
    fn enable_loop(&self) -> PyResult<()> {
        handle_track_result(self.track_handle.enable_loop())
    }
    /// Disables looping.
    #[pyo3(text_signature = "($self)")]
    fn disable_loop(&self) -> PyResult<()> {
        handle_track_result(self.track_handle.disable_loop())
    }
    /// Loops for a certain amount of times.
    #[pyo3(text_signature = "($self, count)")]
    fn loop_for(&self, count: usize) -> PyResult<()> {
        handle_track_result(self.track_handle.loop_for(count))
    }
    #[getter]
    fn uuid(&self) -> String {
        self.track_handle.uuid().to_string()
    }
    #[getter]
    fn metadata(&self) -> PyMetadata {
        let md = &self.track_handle.metadata();
        PyMetadata {
            track: md.track.clone(),
            artist: md.artist.clone(),
            date: md.date.clone(),
            channels: md.channels,
            channel: md.channel.clone(),
            start_time: unwrap_duration(md.start_time),
            duration: unwrap_duration(md.duration),
            sample_rate: md.sample_rate,
            source_url: md.source_url.clone(),
            title: md.title.clone(),
            thumbnail: md.thumbnail.clone(),
        }
    }
}
