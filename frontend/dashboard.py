import streamlit as st

st.set_page_config(page_title="Data Visualizations Dashboard")

st.title("Data Visualizations Dashboard")

st.markdown("""
    <p>This dashboard displays various data visualizations related to the Crowd Emotion Recognition project.</p>
""", unsafe_allow_html=True)

# Paths to saved plots
plot_files = [
    "plots/distribution_of_images_per_class.png",
    # "plots/example_images_before_augmentation.png",
    # "plots/example_images_after_augmentation.png",
    # "plots/training_validation_accuracy.png",
    # "plots/training_validation_loss.png",
    "plots/confusion_matrix.png",
    # "plots/classification_report.png",
    # "plots/image_count_per_class_before_augmentation.png",
    # "plots/image_count_per_class_after_augmentation.png",
    # "plots/augmentation_effects.png",
    # "plots/emotion_distribution_training_vs_testing.png",
    # "plots/sample_misclassified_images.png",
    # "plots/average_emotion_distribution_across_batches.png",
    # "plots/roc_curves_for_each_class.png"
]

# Display plots in two columns
for i in range(0, len(plot_files), 2):
    cols = st.columns(2)
    for col, plot_file in zip(cols, plot_files[i:i+2]):
        col.image(plot_file, use_column_width=True)

st.markdown("""
    <style>
    .footer {
        position: relative;
        bottom: 0;
        width: 100%;
        text-align: center;
    }
    </style>
    <div class="footer">
        <p><b>The future of emotional intelligence | Crowd Emotion Recognizer | Developed by Zunaira and Darban |</b></p>
        <p><b>Supervised by Dr. Ali Raza!</b></p>
    </div>
""", unsafe_allow_html=True)