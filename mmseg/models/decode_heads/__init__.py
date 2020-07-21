from .ann_head import ANNHead
from .aspp_head import ASPPHead
from .cc_head import CCHead
from .da_head import DAHead
from .enc_head import EncHead
from .fcn_head import FCNHead
from .fpn_decode_head import FpnDecodeHead
from .gc_head import GCHead
from .nl_head import NLHead
from .ocr_head import OCRHead, OCRHeadV2
from .ocrplus_head import OCRPlusHead, OCRPlusHeadV2
from .psa_head import PSAHead
from .psp_head import PSPHead
from .sep_aspp_head import DepthwiseSeparableASPPHead
from .uper_head import UPerHead

__all__ = [
    'FCNHead', 'PSPHead', 'ASPPHead', 'PSAHead', 'NLHead', 'GCHead', 'CCHead',
    'UPerHead', 'DepthwiseSeparableASPPHead', 'ANNHead', 'DAHead', 'OCRHead',
    'EncHead', 'OCRPlusHead', 'OCRPlusHeadV2', 'OCRHeadV2', 'FpnDecodeHead'
]