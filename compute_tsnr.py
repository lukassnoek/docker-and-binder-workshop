import os
import sys
import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
from nilearn import masking, plotting, image


def main(file=None, mask=True, figure=False, out_dir=None):
    """ Computes the median temporal signal-to-noise ratio (TSNR) of
    a 4D fMRI file (similar to what MRIQC does).

    Parameters
    ----------
    file : str or None
        If str, refers to the path of a 4D nifti file. If None,
        a default file is loaded.
    mask : bool
        Whether to mask the file (using Nilearn)
    figure : bool
        If False, only prints out the median TSNR value. If True,
        it will write out a figure with voxel-wise TSNR values.
    out_dir : str
        Directory to save TSNR figure to. If None, the same directory
        as `file` will be used.
    """

    if file is None:
        print("WARNING: you did not specify a file! Exiting ...")
        sys.exit()

    print(f"INFO: computing TSNR for {file}")
    
    # Load in image and associated data
    img = image.load_img(file)

    # Apply mask
    if mask:
        print("INFO: computing EPI mask")
        mask = masking.compute_epi_mask(img)
    else:
        # If no mask, at least remove zeros
        nonzeros = (img.get_fdata().sum(axis=3) != 0).astype(int)
        mask = nib.Nifti1Image(nonzeros, affine=img.affine)

    img_2d = masking.apply_mask(img, mask)

    # Compute TSNR
    tsnr = np.mean(img_2d, axis=0) / np.std(img_2d, axis=0)
    print(f"INFO: median TSNR = {np.median(tsnr):.3f}")

    if figure:
        # Recreate 3D nifti + plot with Nilearn
        tsnr_img = masking.unmask(tsnr, mask_img=mask)
        plotting.plot_epi(tsnr_img)
        
        # Save to disk
        if out_dir is None:  # set dir if necessary
            out_dir = os.path.dirname(file)

        f_name = os.path.basename(file).replace('.nii.gz', '_tsnr.png')
        f_out = os.path.join(out_dir, f_name)
        print(f"INFO: Saving figure to {f_out}")
        plt.savefig(f_out)


if __name__ == '__main__':

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('f', type=str, nargs='?', default=None, help='File to compute TSNR of.')
    parser.add_argument('--mask', action='store_true', help='Whether to apply a functional mask.')
    parser.add_argument('--figure', action='store_true', help='Whether to output a voxelwise TSNR figure.')
    args = parser.parse_args()

    main(args.f, args.mask, args.figure)