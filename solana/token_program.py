"""Library to interface with SPL tokens on Solana."""

from enum import Enum
from typing import List, NamedTuple, Optional

from solana.instruction import InstructionLayout
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction
from solana.utils.helpers import from_uint8_bytes

# Instruction Indices
_INITIALIZE_MINT = 0
_INITIALIZE_ACCOUNT = 1
_INITIALIZE_MULTISIG = 2
_TRANSFER = 3
_APPROVE = 4
_REVOKE = 5
_SET_AUTHORITY = 6
_MINT_TO = 7
_BURN = 8
_CLOSE_ACCOUNT = 9
_FREEZE_ACCOUNT = 10
_THAW_ACCOUNT = 11
_TRANSFER2 = 12
_APPROVE2 = 13
_MINT_TO2 = 14
_BURN2 = 15


class AuthorityType(Enum):
    """Specifies the authority type for SetAuthority instructions."""

    MintTokens = 0
    """"Authority to mint new tokens."""
    FreezeAccount = 1
    """Authority to freeze any account associated with the Mint."""
    AccountOwner = 2
    """Owner of a given token account."""
    CloseAccount = 3
    """Authority to close a token account."""


# Instruction Params
class InitializeMintParams(NamedTuple):
    """Initialize token mint transaction params."""

    token_program_id: PublicKey
    """"""
    mint: PublicKey
    """Public key of the minter."""
    mint_authority: PublicKey
    """The authority/multisignature to mint tokens."""
    freeze_authority: Optional[PublicKey]
    """The freeze authority/multisignature of the mint."""
    decimals: int
    """Number of base 10 digits to the right of the decimal place."""


class InitializeAccountParams(NamedTuple):
    """Initialize token account transaction params."""

    token_program_id: PublicKey
    """"""
    account: PublicKey
    """"""
    mint: PublicKey
    """"""
    owner: PublicKey
    """"""


class InitializeMultisigParams(NamedTuple):
    """Initialize multisig token account transaction params."""

    token_program_id: PublicKey
    """"""
    multisig: PublicKey
    """"""
    signers: List[PublicKey]
    """"""
    m: int
    """The number of signers (M) required to validate this multisignature account."""


class TransferParams(NamedTuple):
    """Transfer token transaction params."""

    token_program_id: PublicKey
    """"""
    source: PublicKey
    """"""
    destination: PublicKey
    """"""
    authority: PublicKey
    """"""
    signers: List[PublicKey]
    """"""
    amount: int
    """"""


class ApproveParams(NamedTuple):
    """Approve token transaction params."""

    token_program_id: PublicKey
    """"""
    source: PublicKey
    """"""
    delegate: PublicKey
    """"""
    owner: PublicKey
    """"""
    signers: List[PublicKey]
    """"""
    amount: int
    """"""


class RevokeParams(NamedTuple):
    """Revoke token transaction params."""

    token_program_id: PublicKey
    """"""
    source: PublicKey
    """"""
    owner: PublicKey
    """"""
    signers: List[PublicKey]
    """"""


class SetAuthorityParams(NamedTuple):
    """Set token authority transaction params."""

    authority: AuthorityType
    """The type of authority to update."""
    new_authority: Optional[PublicKey] = None
    """The new authority."""


class MintToParams(NamedTuple):
    """Mint token transaction params."""

    token_program_id: PublicKey
    """"""
    mint: PublicKey
    """"""
    account: PublicKey
    """"""
    owner: PublicKey
    """"""
    signers: List[PublicKey]
    """"""
    amount: int
    """"""


class BurnParams(NamedTuple):
    """Burn token transaction params."""

    token_program_id: PublicKey
    """"""
    account: PublicKey
    """"""
    mint: PublicKey
    """"""
    authority: PublicKey
    """"""
    signers: List[PublicKey]
    """"""
    amount: int
    """"""


class CloseAccountParams(NamedTuple):
    """Close token account transaction params."""

    token_program_id: PublicKey
    """"""
    account: PublicKey
    """"""
    destination: PublicKey
    """"""
    owner: PublicKey
    """"""
    signers: List[PublicKey]
    """"""


class FreezeAccountParams(NamedTuple):
    """Freeze token account transaction params."""

    token_program_id: PublicKey
    """"""
    account: PublicKey
    """"""
    mint: PublicKey
    """"""
    owner: PublicKey
    """"""
    signers: List[PublicKey]
    """"""


class ThawAccountParams(NamedTuple):
    """Thaw token account transaction params."""

    token_program_id: PublicKey
    """"""
    account: PublicKey
    """"""
    mint: PublicKey
    """"""
    owner: PublicKey
    """"""
    signers: List[PublicKey]
    """"""


class Transfer2Params(NamedTuple):
    """Transfer2 token transaction params."""

    token_program_id: PublicKey
    """"""
    mint: PublicKey
    """"""
    source: PublicKey
    """"""
    destination: PublicKey
    """"""
    authority: PublicKey
    """"""
    signers: List[PublicKey]
    """"""
    amount: int
    """"""
    decimal: int
    """"""


class Approve2Params(NamedTuple):
    """Approve2 token transaction params."""

    token_program_id: PublicKey
    """"""
    mint: PublicKey
    """"""
    source: PublicKey
    """"""
    delegate: PublicKey
    """"""
    owner: PublicKey
    """"""
    signers: List[PublicKey]
    """"""
    amount: int
    """"""
    decimal: int
    """"""


class MintTo2Params(NamedTuple):
    """MintTo2 token transaction params."""

    token_program_id: PublicKey
    """"""
    mint: PublicKey
    """"""
    account: PublicKey
    """"""
    owner: PublicKey
    """"""
    signers: List[PublicKey]
    """"""
    amount: int
    """"""
    decimal: int
    """"""


class Burn2Params(NamedTuple):
    """Burn2 token transaction params."""

    token_program_id: PublicKey
    """"""
    mint: PublicKey
    """"""
    account: PublicKey
    """"""
    owner: PublicKey
    """"""
    signers: List[PublicKey]
    """"""
    amount: int
    """"""
    decimal: int
    """"""


TOKEN_INSTRUCTION_LAYOUTS: List[InstructionLayout] = [
    InstructionLayout(idx=_INITIALIZE_MINT, fmt="B32s32s"),
    InstructionLayout(idx=_INITIALIZE_ACCOUNT, fmt=""),
    InstructionLayout(idx=_INITIALIZE_MULTISIG, fmt="B"),
    InstructionLayout(idx=_TRANSFER, fmt="Q"),
    InstructionLayout(idx=_APPROVE, fmt="Q"),
    InstructionLayout(idx=_REVOKE, fmt=""),
    InstructionLayout(idx=_SET_AUTHORITY, fmt="I32s"),
    InstructionLayout(idx=_MINT_TO, fmt="Q"),
    InstructionLayout(idx=_BURN, fmt="Q"),
    InstructionLayout(idx=_CLOSE_ACCOUNT, fmt=""),
    InstructionLayout(idx=_FREEZE_ACCOUNT, fmt=""),
    InstructionLayout(idx=_THAW_ACCOUNT, fmt=""),
    InstructionLayout(idx=_TRANSFER2, fmt="QB"),
    InstructionLayout(idx=_APPROVE2, fmt="QB"),
    InstructionLayout(idx=_MINT_TO2, fmt="QB"),
    InstructionLayout(idx=_BURN2, fmt="QB"),
]


def decode_instruction_layout(instruction: TransactionInstruction) -> InstructionLayout:
    """Decode a token instruction and retrieve the instruction layout."""
    # Slice the first 4 bytes to get the type
    type_data = instruction.data[:4]
    type_idx = from_uint8_bytes(type_data)
    if 0 <= type_idx < len(TOKEN_INSTRUCTION_LAYOUTS):
        return TOKEN_INSTRUCTION_LAYOUTS[type_idx]
    raise ValueError("unknown transaction instruction")


def decode_initialize_mint(instruction: TransactionInstruction) -> InitializeMintParams:
    """Decode an initialize mint token instruction and retrieve the instruction params."""
    raise NotImplementedError("decode_initialize_mint not implemented")


def decode_initialize_account(instruction: TransactionInstruction) -> InitializeAccountParams:
    """Decode an initialize account token instruction and retrieve the instruction params."""
    raise NotImplementedError("decode_initialize_account not implemented")


def decode_initialize_multisig(instruction: TransactionInstruction) -> InitializeMultisigParams:
    """Decode an initialize multisig account token instruction and retrieve the instruction params."""
    raise NotImplementedError("decode_initialize_multisig not implemented")


def decode_token_transfer(instruction: TransactionInstruction) -> TransferParams:
    """Decode a transfer token transaction and retrieve the instruction params."""
    raise NotImplementedError("decode_token_transfer not implemented")


def decode_approve(instruction: TransactionInstruction) -> ApproveParams:
    """Decode a approve token transaction and retrieve the instruction params."""
    raise NotImplementedError("decode_token_approve not implemented")


def decode_revoke(instruction: TransactionInstruction) -> RevokeParams:
    """Decode a revoke token transaction and retrieve the instruction params."""
    raise NotImplementedError("decode_token_revoke not implemented")


def decode_set_authority(instruction: TransactionInstruction) -> SetAuthorityParams:
    """Decode a set authority token transaction and retrieve the instruction params."""
    raise NotImplementedError("decode_set_authority not implemented")


def decode_mint_to(instruction: TransactionInstruction) -> MintToParams:
    """Decode a mint to token transaction and retrieve the instruction params."""
    raise NotImplementedError("decode_mint_to not implemented")


def decode_burn(instruction: TransactionInstruction) -> BurnParams:
    """Decode a burn token transaction and retrieve the instruction params."""
    raise NotImplementedError("decode_burn not implemented")


def decode_close_account(instruction: TransactionInstruction) -> CloseAccountParams:
    """Decode a close account token transaction and retrieve the instruction params."""
    raise NotImplementedError("decode_close_account not implemented")


def decode_thaw_account(instruction: TransactionInstruction) -> ThawAccountParams:
    """Decode a thaw account token transaction and retrieve the instruction params."""
    raise NotImplementedError("decode_thaw_account not implemented")


def decode_token_transfer2(instruction: TransactionInstruction) -> Transfer2Params:
    """Decode a transfer2 token transaction and retrieve the instruction params."""
    raise NotImplementedError("decode_transfer2 not implemented")


def decode_approve2(instruction: TransactionInstruction) -> Transfer2Params:
    """Decode a approve2 token transaction and retrieve the instruction params."""
    raise NotImplementedError("decode_approve2 not implemented")


def decode_mint_to2(instruction: TransactionInstruction) -> MintTo2Params:
    """Decode a mintTo2 token transaction and retrieve the instruction params."""
    raise NotImplementedError("decode_mint_to2 not implemented")


def decode_burn2(instruction: TransactionInstruction) -> MintTo2Params:
    """Decode a burn2 token transaction and retrieve the instruction params."""
    raise NotImplementedError("decode_burn2 not implemented")