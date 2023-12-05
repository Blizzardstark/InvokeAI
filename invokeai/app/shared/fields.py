class FieldDescriptions:
    denoising_start = "When to start denoising, expressed a percentage of total steps"
    denoising_end = "When to stop denoising, expressed a percentage of total steps"
    cfg_scale = "Classifier-Free Guidance scale"
    cfg_rescale_multiplier = "Rescale multiplier for CFG guidance, used for models trained with zero-terminal SNR"
    scheduler = "Scheduler to use during inference"
    positive_cond = "Positive conditioning tensor"
    negative_cond = "Negative conditioning tensor"
    noise = "Noise tensor"
    clip = "CLIP (tokenizer, text encoder, LoRAs) and skipped layer count"
    unet = "UNet (scheduler, LoRAs)"
    vae = "VAE"
    cond = "Conditioning tensor"
    controlnet_model = "ControlNet model to load"
    vae_model = "VAE model to load"
    lora_model = "LoRA model to load"
    main_model = "Main model (UNet, VAE, CLIP) to load"
    sdxl_main_model = "SDXL Main model (UNet, VAE, CLIP1, CLIP2) to load"
    sdxl_refiner_model = "SDXL Refiner Main Modde (UNet, VAE, CLIP2) to load"
    onnx_main_model = "ONNX Main model (UNet, VAE, CLIP) to load"
    lora_weight = "The weight at which the LoRA is applied to each model"
    compel_prompt = "Prompt to be parsed by Compel to create a conditioning tensor"
    raw_prompt = "Raw prompt text (no parsing)"
    sdxl_aesthetic = "The aesthetic score to apply to the conditioning tensor"
    skipped_layers = "Number of layers to skip in text encoder"
    seed = "Seed for random number generation"
    steps = "Number of steps to run"
    width = "Width of output (px)"
    height = "Height of output (px)"
    control = "ControlNet(s) to apply"
    ip_adapter = "IP-Adapter to apply"
    t2i_adapter = "T2I-Adapter(s) to apply"
    denoised_latents = "Denoised latents tensor"
    latents = "Latents tensor"
    strength = "Strength of denoising (proportional to steps)"
    metadata = "Optional metadata to be saved with the image"
    metadata_collection = "Collection of Metadata"
    metadata_item_polymorphic = "A single metadata item or collection of metadata items"
    metadata_item_label = "Label for this metadata item"
    metadata_item_value = "The value for this metadata item (may be any type)"
    workflow = "Optional workflow to be saved with the image"
    interp_mode = "Interpolation mode"
    torch_antialias = "Whether or not to apply antialiasing (bilinear or bicubic only)"
    fp32 = "Whether or not to use full float32 precision"
    precision = "Precision to use"
    tiled = "Processing using overlapping tiles (reduce memory consumption)"
    detect_res = "Pixel resolution for detection"
    image_res = "Pixel resolution for output image"
    safe_mode = "Whether or not to use safe mode"
    scribble_mode = "Whether or not to use scribble mode"
    scale_factor = "The factor by which to scale"
    blend_alpha = (
        "Blending factor. 0.0 = use input A only, 1.0 = use input B only, 0.5 = 50% mix of input A and input B."
    )
    num_1 = "The first number"
    num_2 = "The second number"
    mask = "The mask to use for the operation"
    board = "The board to save the image to"
    image = "The image to process"
    tile_size = "Tile size"
    inclusive_low = "The inclusive low value"
    exclusive_high = "The exclusive high value"
    decimal_places = "The number of decimal places to round to"
    freeu_s1 = 'Scaling factor for stage 1 to attenuate the contributions of the skip features. This is done to mitigate the "oversmoothing effect" in the enhanced denoising process.'
    freeu_s2 = 'Scaling factor for stage 2 to attenuate the contributions of the skip features. This is done to mitigate the "oversmoothing effect" in the enhanced denoising process.'
    freeu_b1 = "Scaling factor for stage 1 to amplify the contributions of backbone features."
    freeu_b2 = "Scaling factor for stage 2 to amplify the contributions of backbone features."
