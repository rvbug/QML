// add plotters in Cargo.toml file:
// [dependencies]
// plotters = "0.3.0"

use plotters::prelude::*;
use std::f64::consts::SQRT_2;

/// Calculate wormhole distance with time dilation effect
/// d = c * t / sqrt(1 - v²/c²)
/// 
/// # Arguments
/// * `c` - Speed of light
/// * `t` - Time
/// * `v` - Velocity
fn wormhole_distance(c: f64, t: f64, v: f64) -> f64 {
    let time_dilation = 1.0 / (1.0 - (v / c).powi(2)).sqrt();
    c * t * time_dilation
}

/// Generate data points for wormhole distance visualization
fn generate_distance_data() -> Vec<(f64, f64)> {
    let c = 299_792_458.0; // Speed of light in m/s
    let mut data_points = Vec::new();

    // Generate points for different velocities
    for v_percent in 0..=100 {
        let v = c * (v_percent as f64 / 100.0);
        let time = 1.0; // 1 second
        let distance = wormhole_distance(c, time, v);
        data_points.push((v_percent as f64, distance / c));
    }

    data_points
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Create a drawing area
    let root = BitMapBackend::new("wormhole_distance_plot.png", (800, 600)).into_drawing_area();
    root.fill(&WHITE)?;

    let data = generate_distance_data();

    // Find max and min for proper scaling
    let max_distance = data.iter().map(|&(_, d)| d).fold(f64::NEG_INFINITY, f64::max);
    let min_distance = data.iter().map(|&(_, d)| d).fold(f64::INFINITY, f64::min);

    let mut chart = ChartBuilder::on(&root)
        .caption("Wormhole Distance vs Velocity", ("Arial", 30).into_font())
        .margin(20)
        .x_label_area_size(40)
        .y_label_area_size(60)
        .build_cartesian_2d(0.0..100.0, min_distance..max_distance)?;

    chart
        .configure_mesh()
        .x_desc("Velocity (% of light speed)")
        .y_desc("Normalized Distance")
        .draw()?;

    chart.draw_series(
        data.iter().map(|&(x, y)| Circle::new((x, y), 5, GREEN.filled()))
    )?;

    chart.draw_series(
        LineSeries::new(
            data.iter().cloned().map(|(x, y)| (x, y)),
            &RED
        )
    )?;

    root.present()?;

    println!("Wormhole distance visualization saved as 'wormhole_distance_plot.png'");
    Ok(())
}
