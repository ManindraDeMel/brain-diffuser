import os

# Download Experiment Infos
os.system('aws s3 cp --no-sign-request s3://natural-scenes-dataset/nsddata/experiments/nsd/nsd_expdesign.mat nsddata/experiments/nsd/')
os.system('aws s3 cp --no-sign-request s3://natural-scenes-dataset/nsddata/experiments/nsd/nsd_stim_info_merged.pkl nsddata/experiments/nsd/')

# Download Stimuli
os.system('aws s3 cp --no-sign-request s3://natural-scenes-dataset/nsddata_stimuli/stimuli/nsd/nsd_stimuli.hdf5 nsddata_stimuli/stimuli/nsd/')

# Download Betas
for sub in [1, 2, 5, 7]:
    for sess in range(1, 38):
        os.system(
            f'aws s3 cp --no-sign-request '
            f's3://natural-scenes-dataset/nsddata_betas/ppdata/subj{sub:02d}/func1pt8mm/betas_fithrf_GLMdenoise_RR/betas_session{sess:02d}.nii.gz '
            f'nsddata_betas/ppdata/subj{sub:02d}/func1pt8mm/betas_fithrf_GLMdenoise_RR/'
        )

# Download ROIs
for sub in [1, 2, 5, 7]:
    os.system(
        f'aws s3 cp --no-sign-request '
        f's3://natural-scenes-dataset/nsddata/ppdata/subj{sub:02d}/func1pt8mm/roi/ '
        f'nsddata/ppdata/subj{sub:02d}/func1pt8mm/roi/ --recursive'
    )
