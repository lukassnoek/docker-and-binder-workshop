import sys
import numpy as np
import nibabel as nib
from nilearn import masking, plotting, image
import matplotlib.pyplot as plt


def main(file=None, mask=True, map=False):
    """ Computes the temporal signal-to-noise ratio (TSNR) of
    a 4D fMRI file.

    Parameters
    ----------
    file : str or None
        If str, refers to the path of a 4D nifti file. If None,
        a default file is loaded.
    mask : bool
        Whether to mask the file (using Nilearn)
    map : bool
        If False, only prints out the median TSNR value. If True,
        it will write out a figure with voxel-wise TSNR values.  
    """

    if file is None:
        print("WARNING: you did not specify a file! Exiting ...")
        sys.exit()

    print(f"INFO: computing TSNR for {file}.")
    
    # Load in image and associated data
    img = image.load_img(file)

    # Apply mask
    if mask:
        mask = masking.compute_epi_mask(img)
    else:
        mask = nib.Nifti1Image((img.get_fdata().sum(axis=3) != 0).astype(int), affine=img.affine)

    img_2d = masking.apply_mask(img, mask)

    # Compute TSNR
    tsnr = np.mean(img_2d, axis=0) / np.std(img_2d, axis=0)
    print(f"INFO: median TSNR = {np.median(tsnr):.3f}")

    if map:
        tsnr_img = masking.unmask(tsnr, mask_img=mask)
        plotting.plot_epi(tsnr_img)
        plt.savefig(file.replace('.nii.gz', '_tsnr.png'))


if __name__ == '__main__':

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('f', type=str, nargs='?', default=None, help='File to compute TSNR of.')
    parser.add_argument('--mask', action='store_true', help='Whether to apply a functional mask.')
    parser.add_argument('--map', action='store_true', help='Whether to output a voxelwise TSNR map.')
    args = parser.parse_args()
    
    main(args.f, args.mask, args.map)