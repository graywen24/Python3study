def perform_timed_write(num_bytes, blocksize, fd):
    """
    This function writes to file and records the time

    The function has three steps. The first is to write, the second is to
    record time, and the third is to calculate the rate.

    Parameters
    ----------
    num_bytes: int
        blocksize that needs to be written to the file
    fd: string
        location on filesystem to write to

    Returns
    -------
    bytes_per_second: float
        rate of transfer
    """
    # generate random string
    random_byte_string = os.urandom(blocksize)

    # open the file
    write_file = os.open(fd, os.O_CREAT | os.O_WRONLY | os.O_NONBLOCK)        
    # set time, write, record time
    bytes_written = 0
    before_write = time.clock()
    while bytes_written < num_bytes:
        os.write(write_file, random_byte_string)
        bytes_written += blocksize
    after_write = time.clock()

    #close the file
    os.close(write_file)

    # calculate elapsed time
    elapsed_time = after_write - before_write

    # calculate bytes per second
    bytes_per_second = num_bytes / elapsed_time


    return bytes_per_second