import functools

# import accelerate
import GPUtil
import torch
import torchutil

import {{cookiecutter.project_slug}}


###############################################################################
# Train
###############################################################################


@torchutil.notify('train')
def train(datasets, directory={{cookiecutter.project_slug}}.RUNS_DIR / {{cookiecutter.project_slug}}.CONFIG):
    """Train a model"""
    # Create output directory
    directory.mkdir(parents=True, exist_ok=True)

    #######################
    # Create data loaders #
    #######################

    torch.manual_seed({{cookiecutter.project_slug}}.RANDOM_SEED)
    train_loader = {{cookiecutter.project_slug}}.data.loader(datasets, 'train')
    valid_loader = {{cookiecutter.project_slug}}.data.loader(datasets, 'valid')

    #################
    # Create models #
    #################

    model = {{cookiecutter.project_slug}}.Model()

    ####################
    # Create optimizer #
    ####################

    optimizer = torch.optim.Adam(model.parameters())

    ##############################
    # Maybe load from checkpoint #
    ##############################

    path = torchutil.checkpoint.latest_path(directory)

    if path is not None:

        # Load model
        model, optimizer, state = torchutil.checkpoint.load(
            path,
            model,
            optimizer)
        step, epoch = state['step'], state['epoch']

    else:

        # Train from scratch
        step, epoch = 0, 0

    ####################
    # Device placement #
    ####################

    # uncomment to use accelerate
    # accelerator = accelerate.Accelerator(mixed_precision='fp16')
    # model, optimizer, train_loader, valid_loader = accelerator.prepare(
    #     model,
    #     optimizer,
    #     train_loader,
    #     valid_loader)

    #########
    # Train #
    #########

    # Setup progress bar
    progress = torchutil.iterator(
        range(step, {{cookiecutter.project_slug}}.STEPS),
        f'Training {{"{" ~ cookiecutter.project_slug}}.CONFIG}',
        step,
        {{cookiecutter.project_slug}}.STEPS)

    while step < {{cookiecutter.project_slug}}.STEPS:

        for batch in train_loader:

            # TODO - Unpack batch
            () = batch

            # Forward pass
            () = model(
                # TODO - args
            )

            # Compute loss
            losses = loss(
                # TODO - args
            )

            ##################
            # Optimize model #
            ##################

            # Zero gradients
            optimizer.zero_grad()

            # Backward pass
            losses.backward()

            # Update weights
            optimizer.step()

            ############
            # Evaluate #
            ############

            if step % {{cookiecutter.project_slug}}.EVALUATION_INTERVAL == 0:
                # Raise if GPU tempurature exceeds 90 C
                if any(gpu.temperature > 90. for gpu in GPUtil.getGPUs()):
                    raise RuntimeError(f'GPU is overheating. Terminating training.')
                with {{cookiecutter.project_slug}}.inference_context(model):
                    evaluation_steps = (
                        None if step == {{cookiecutter.project_slug}}.STEPS
                        else {{cookiecutter.project_slug}}.DEFAULT_EVALUATION_STEPS)
                    evaluate_fn = functools.partial(
                        evaluate,
                        directory,
                        step,
                        model,
                        #accelerator,
                        evaluation_steps=evaluation_steps)
                    evaluate_fn('train', train_loader)
                    evaluate_fn('valid', valid_loader)

            ###################
            # Save checkpoint #
            ###################

            if step and step % {{cookiecutter.project_slug}}.CHECKPOINT_INTERVAL == 0:
                torchutil.checkpoint.save(
                    directory / f'{step:08d}.pt',
                    model,
                    optimizer,
                    #accelerator=accelerator,
                    step=step,
                    epoch=epoch)

            ########################
            # Termination criteria #
            ########################

            # Finished training
            if step >= {{cookiecutter.project_slug}}.STEPS:
                break

            ###########
            # Updates #
            ###########

            # Update progress bar
            progress.update()

            # Update training step count
            step += 1

        # Update epoch
        epoch += 1

    # Close progress bar
    progress.close()

    # Save final model
    torchutil.checkpoint.save(
        directory / f'{step:08d}.pt',
        model,
        optimizer,
        #accelerator=accelerator,
        step=step,
        epoch=epoch)


###############################################################################
# Evaluation
###############################################################################


def evaluate(
    directory,
    step,
    model,
    accelerator,
    condition,
    loader,
    evaluation_steps=None
):
    """Perform model evaluation"""
    # Setup evaluation metrics
    metrics = {{cookiecutter.project_slug}}.evaluate.Metrics()

    for i, batch in enumerate(loader):

        # TODO - unpack batch
        () = batch

        # Forward pass
        () = model(
            # TODO - args
        )

        # Update metrics
        metrics.update(
            # TODO - args
        )

        # Stop when we exceed some number of batches
        if evaluation_steps is not None and i + 1 == evaluation_steps:
            break

    # Format results
    scalars = {
        f'{key}/{condition}': value for key, value in metrics().items()}

    # Write to tensorboard
    torchutil.tensorboard.update(directory, step, scalars=scalars)


###############################################################################
# Loss function
###############################################################################


def loss(logits, target):
    """Compute loss function"""
    # TODO
    pass
